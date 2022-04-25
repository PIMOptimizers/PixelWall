import sys

import cvzone
import os
import random
import cv2
import mediapipe as mp
from time import sleep
from threading import *

import pygame
import os
import time
import random

pygame.font.init()

xGlobal = 0.5
yGlobal = 0.5
CoefGlobal = 600.00
ShootGlobal = 0.5
score = 0


class Detection(Thread):
    def run(self):
        global xGlobal
        global yGlobal
        global CoefGlobal
        global ShootGlobal

        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_pose = mp.solutions.pose
        # For webcam input:
        cap = cv2.VideoCapture(0)
        with mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                success, image = cap.read()
                # print("HELLO")
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)

                # Draw the pose annotation on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # if mp_pose.PoseLandmark.value(25) != None:
                # mp_pose.PoseLandmark.value(25)
                # mp_pose.PoseLandmark.value(25)

                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('Detection', cv2.flip(image, 1))  # Responsable affichage du camera
                # if results.pose_landmarks in np.array(0,1,2,3,4,5,6,7,8,9,10,11,12) :
                # print(type(results.pose_landmarks[0]))
                # if mp_pose.PoseLandmark.LEFT_EAR == True :
                # print(results.pose_landmarks.landmark[0])

                keypoints = []
                # PositionGlobal = results.pose_landmarks.landmark[0].y
                # print(type(PositionGlobal))
                # print(type(results.pose_landmarks.landmark[0].y))
                if results.pose_landmarks:
                    # if results.pose_landmarks.landmark[0].y < 0.5:
                    # print("duck")
                    # print(("%.2f" % results.pose_landmarks.landmark[0].y))
                    # yGlobal=str(round(results.pose_landmarks.landmark[0].y, 2))
                    # yGlobal = float(yGlobal) * float(CoefGlobal)
                    # float(yGlobal)
                    # print(yGlobal)
                    # else:
                    # if results.pose_landmarks.landmark[0].y > 0.7:
                    # print("%.2f" % results.pose_landmarks.landmark[0].y)
                    # yGlobal=str(round(results.pose_landmarks.landmark[0].y, 2))
                    # yGlobal = float(yGlobal) * float(CoefGlobal)
                    # float(yGlobal)
                    # print(yGlobal)

                    # else:
                    # print(results.pose_landmarks.landmark[0].y)
                    # print(PositionGlobal)
                    # print("%.2f" % results.pose_landmarks.landmark[0].y)
                    # print("Hello")
                    # print(type(yGlobal))
                    # yGlobal=str(round(results.pose_landmarks.landmark[0].y, 2))
                    # float(yGlobal)
                    # yGlobal = float(yGlobal) * float(CoefGlobal)
                    # print(yGlobal)
                    yGlobal = results.pose_landmarks.landmark[0].y
                    xGlobal = results.pose_landmarks.landmark[0].x
                    ShootGlobal = results.pose_landmarks.landmark[16].x
                    print(ShootGlobal)

                else:

                    print("no nose")

                # print(results.pose_landmarks.landmark[0].y)

                # print(mp_drawing.draw_landmarks())



                if cv2.waitKey(5) & 0xFF == 27:
                    cap.release()
                    cv2.destroyAllWindows()
                    os.system('python ChooseGamePage.py')
                    sys.exit()

        # cap.release()


class Game(Thread):
    def run(self):
        global xGlobal
        global yGlobal
        global ShootGlobal
        WIDTH, HEIGHT = 1200, 720
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders")

        # Load images
        RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
        GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
        BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

        # Player player
        YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

        # Lasers
        RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
        GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
        BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
        YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

        # Background
        BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

        class Laser:
            def __init__(self, x, y, img):
                self.x = x
                self.y = y
                self.img = img
                self.mask = pygame.mask.from_surface(self.img)

            def draw(self, window):
                window.blit(self.img, (self.x, self.y))

            def move(self, vel):
                self.y += vel

            def off_screen(self, height):
                return not (self.y <= height and self.y >= 0)

            def collision(self, obj):
                return collide(self, obj)

        class Ship:
            COOLDOWN = 30

            def __init__(self, x, y, health=100):
                self.x = x
                self.y = y
                self.health = health
                self.ship_img = None
                self.laser_img = None
                self.lasers = []
                self.cool_down_counter = 0

            def draw(self, window):
                window.blit(self.ship_img, (self.x, self.y))
                for laser in self.lasers:
                    laser.draw(window)

            def move_lasers(self, vel, obj):
                self.cooldown()
                for laser in self.lasers:
                    laser.move(vel)
                    if laser.off_screen(HEIGHT):
                        self.lasers.remove(laser)
                    elif laser.collision(obj):
                        obj.health -= 10
                        self.lasers.remove(laser)

            def cooldown(self):
                if self.cool_down_counter >= self.COOLDOWN:
                    self.cool_down_counter = 0
                elif self.cool_down_counter > 0:
                    self.cool_down_counter += 1

            def shoot(self):
                if self.cool_down_counter == 0:
                    laser = Laser(self.x, self.y, self.laser_img)
                    self.lasers.append(laser)
                    self.cool_down_counter = 1

            def get_width(self):
                return self.ship_img.get_width()

            def get_height(self):
                return self.ship_img.get_height()

        class Player(Ship):
            def __init__(self, x, y, health=100):
                super().__init__(x, y, health)
                self.ship_img = YELLOW_SPACE_SHIP
                self.laser_img = YELLOW_LASER
                self.mask = pygame.mask.from_surface(self.ship_img)
                self.max_health = health

            def move_lasers(self, vel, objs):
                self.cooldown()
                for laser in self.lasers:
                    laser.move(vel)
                    if laser.off_screen(HEIGHT):
                        self.lasers.remove(laser)
                    else:
                        for obj in objs:
                            if laser.collision(obj):
                                objs.remove(obj)
                                if laser in self.lasers:
                                    self.lasers.remove(laser)

            def draw(self, window):
                super().draw(window)
                self.healthbar(window)

            def healthbar(self, window):
                pygame.draw.rect(window, (255, 0, 0),
                                 (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
                pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10,
                                                       self.ship_img.get_width() * (self.health / self.max_health), 10))

        class Enemy(Ship):
            COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
            }

            def __init__(self, x, y, color, health=100):
                super().__init__(x, y, health)
                self.ship_img, self.laser_img = self.COLOR_MAP[color]
                self.mask = pygame.mask.from_surface(self.ship_img)

            def move(self, vel):
                self.y += vel

            def shoot(self):
                if self.cool_down_counter == 0:
                    laser = Laser(self.x - 20, self.y, self.laser_img)
                    self.lasers.append(laser)
                    self.cool_down_counter = 1

        def collide(obj1, obj2):
            offset_x = obj2.x - obj1.x
            offset_y = obj2.y - obj1.y
            return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

        def main():
            run = True
            FPS = 60
            level = 0
            lives = 5
            main_font = pygame.font.SysFont("comicsans", 50)
            lost_font = pygame.font.SysFont("comicsans", 60)

            enemies = []
            wave_length = 5
            enemy_vel = 1

            player_vel = 5
            laser_vel = 5
            score = 0

            player = Player(300, 630)

            clock = pygame.time.Clock()

            lost = False
            lost_count = 0

            def redraw_window():
                WIN.blit(BG, (0, 0))
                # draw text
                lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
                score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))

                WIN.blit(lives_label, (10, 10))
                WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
                WIN.blit(score_label, (WIDTH - score_label.get_width() - 10, 50))

                for enemy in enemies:
                    enemy.draw(WIN)

                player.draw(WIN)

                if lost:
                    lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
                    WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

                    # score related
                    score_label = lost_font.render(f"YOU'RE SCORE IS : {score}", 1, (255, 255, 255))
                    WIN.blit(score_label, (WIDTH / 3 - lost_label.get_width() / 2, 420))

                pygame.display.update()

            while run:
                clock.tick(FPS)
                redraw_window()
                # print(player.y)

                if lives <= 0 or player.health <= 0:
                    lost = True
                    lost_count += 1

                if lost:
                    if lost_count > FPS * 3:
                        run = False
                    else:
                        continue

                if len(enemies) == 0:
                    level += 1
                    # score related
                    score += 2
                    print("score =", score)
                    wave_length += 5
                    for i in range(wave_length):
                        enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                      random.choice(["red", "blue", "green"]))
                        enemies.append(enemy)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                # Movement using camera:
                if xGlobal > 0.6:
                    player.x -= player_vel
                if xGlobal < 0.4:
                    player.x += player_vel
                if yGlobal < 0.4:
                    player.y -= player_vel
                if yGlobal > 0.6:
                    player.y += player_vel
                if ShootGlobal > 0.3 and ShootGlobal < 0.6:
                    player.shoot()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] and player.x - player_vel > 0:  # left
                    player.x -= player_vel

                if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
                    player.x += player_vel
                if keys[pygame.K_w] and player.y - player_vel > 0:  # up
                    player.y -= player_vel
                if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
                    player.y += player_vel
                if keys[pygame.K_SPACE]:
                    player.shoot()

                if keys[pygame.K_e]:
                    exit()

                for enemy in enemies[:]:
                    enemy.move(enemy_vel)
                    enemy.move_lasers(laser_vel, player)

                    if random.randrange(0, 2 * 60) == 1:
                        enemy.shoot()

                    if collide(enemy, player):
                        player.health -= 10
                        enemies.remove(enemy)
                    elif enemy.y + enemy.get_height() > HEIGHT:
                        lives -= 1
                        enemies.remove(enemy)

                player.move_lasers(-laser_vel, enemies)

        def main_menu():
            title_font = pygame.font.SysFont("comicsans", 70)
            run = True

            while run:
                # button related

                # separation here
                WIN.blit(BG, (0, 0))
                title_label = title_font.render("Press the mouse to begin", 1, (255, 255, 255))
                WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 250))
                title_label2 = title_font.render("move your head to control", 1, (255, 255, 255))
                WIN.blit(title_label2, (WIDTH / 2.5 - title_label.get_width() / 2.5, 350))
                title_label3 = title_font.render("the ship and your hand to shoot", 1, (255, 255, 255))
                WIN.blit(title_label3, (WIDTH / 3.2 - title_label.get_width() / 3.2, 400))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        main()
            pygame.quit()

        main_menu()


t1 = Detection()
t2 = Game()

t1.start()
t2.start()
