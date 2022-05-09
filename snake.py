import math
import os
import random
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

# play space
cap.set(3, 1280)
cap.set(4, 720)

# background
imgBackground = cv2.imread("./SnakeResources/background.png")


detector = HandDetector(detectionCon=0.8, maxHands=1)

# global g_score
# g_score = 0


class SnakeGameClass:
    def __init__(self, pathFood):
        self.points = []  # all points of the snake
        self.lengths = []  # distance between each point
        self.currentLength = 0  # total length of the snake
        self.allowedLength = 150  # total allowed length
        self.previousHead = 0, 0  # previous head point

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()

        self.score = 0
        self.gameOver = False

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

    def update(self, imgMain, currentHead):

        global g_score

        if self.gameOver:
            cvzone.putTextRect(imgMain, "GAME OVER", [300, 550], scale=7, thickness=5, offset=20)
            cvzone.putTextRect(imgMain, f'YOUR SCORE: {g_score}', [250, 400], scale=7, thickness=5, offset=20)

            cvzone.putTextRect(imgMain, "press R to restart", [100, 100], scale=7, thickness=5, offset=20)

            # score file thing still trying
            score_file = open("score_file.txt", "w+")
            score_file.write(str(g_score))
            score_file.close()

        else:
            px, py = self.previousHead
            cx, cy = currentHead

            self.points.append([cx, cy])
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = cx, cy

            # Length reduction
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                        break

            # Check if food is eaten
            rx, ry = self.foodPoint
            if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                # print("yummy")
                self.randomFoodLocation()
                self.allowedLength += 50
                self.score += 1
                # zedt faza hnaa
                # g_score += 1
                print(self.score)

            # Draw snake
            if self.points:
                for i, point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                cv2.circle(imgMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

            # Draw Food
            imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood // 2, ry - self.hFood // 2))
            g_score = self.score
            cvzone.putTextRect(imgMain, f'SCORE: {self.score}', [50, 80], scale=3, thickness=3, offset=10)

            # Check for Collision
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
            minDistance = cv2.pointPolygonTest(pts, (cx, cy), True)
            # print(minDistance)

            if -1 <= minDistance <= 1:
                print("HIT")
                self.gameOver = True
                self.points = []  # all points of the snake
                self.lengths = []  # distance between each point
                self.currentLength = 0
                self.allowedLength = 150
                self.previousHead = 0, 0
                self.randomFoodLocation()
                self.score = 0

        return imgMain


game = SnakeGameClass("burger.png")

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # background remover
    # img = segmentor.removeBG(img, (0, 0, 0))

    hands, img = detector.findHands(img, flipType=False)

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

    if hands:
        lmList = hands[0]['lmList']
        # position of index finger
        pointIndex = lmList[8][0:2]
        img = game.update(img, pointIndex)

    cv2.imshow("Snake Game - PIXELL WALL", img)

    key = cv2.waitKey(1)
    if key == ord('r'):
        game.gameOver = False

    if key == ord('f') or key == 27:
        # exit()
        cap.release()
        cv2.destroyAllWindows()
        os.system('python ChooseGamePage.py')
