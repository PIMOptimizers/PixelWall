import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

os.environ['SDL_VIDEO_WINDOW_POS'] = "120,30"

# Importing all images
imgBackground = cv2.imread("./PingPongResources/Background.png")
imgBall = cv2.imread("./PingPongResources/ball-resized.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread("./PingPongResources/bat1-resized.png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread("./PingPongResources/bat2-resized.png", cv2.IMREAD_UNCHANGED)
imgGameOver = cv2.imread("./PingPongResources/gameOver.png")

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
ballPos = [100, 100]
speedX = 10
speedY = 10
gameOver = False
score = [0, 0]

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    # Find the hand and its landmarks
    hands, img = detector.findHands(img, flipType=False)  # with draw

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

    # Check for hands
    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']
            # w1 = 90
            # h1 = 90
            h1, w1, _ = imgBat1.shape
            y1 = y - h1//2
            y1 = np.clip(y1, 20, 470)

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgBat1, (20, y1))
                if 45 < ballPos[0] < 45 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] += 80
                    score[0] += 1

            if hand['type'] == "Right":
                img = cvzone.overlayPNG(img, imgBat2, (1160, y1))
                if 1080 < ballPos[0] < 1200 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] -= 80
                    score[1] += 1

    # Game Over
    if ballPos[0] < 40 or ballPos[0] > 1200:
        gameOver = True
    if gameOver:
        img = imgGameOver
        cv2.putText(img, str(score[1] + score[0]).zfill(2), (585, 380), cv2.FONT_HERSHEY_COMPLEX, 2.5, (200, 0, 200), 5)

    # If game not over move the ball
    else:
        # Move the  ball
        if ballPos[1] >= 550 or ballPos[1] <= 5:
            speedY = -speedY

        ballPos[0] += speedX
        ballPos[1] += speedY

        # Draw the ball
        img = cvzone.overlayPNG(img, imgBall, ballPos)

        cv2.putText(img, str(score[0]), (300, 690), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(score[1]), (900, 690), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    cv2.imshow("Ping Pong", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        ballPos = [100, 100]
        speedX = 10
        speedY = 10
        gameOver = False
        score = [0, 0]
        imgGameOver = cv2.imread("./PingPongResources/gameOver.png")
