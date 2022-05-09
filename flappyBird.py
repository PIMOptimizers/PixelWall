import sys
import time
import random
import pygame
from collections import deque
import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
pygame.init()

# Initialize required elements/environment
VID_CAP = cv.VideoCapture(0)

# Trying to import background and merge it with the camera
imgBackground = cv.imread("./FlappyBirdResources/flappy_background.png")
# Check cap.read

# game over thing
imgGameOver = pygame.image.load(r'./PingPongResources/gameOver.png')

# Trying to resize the window
VID_CAP.set(3, 1280)
VID_CAP.set(4, 720)

window_size = (VID_CAP.get(cv.CAP_PROP_FRAME_WIDTH), VID_CAP.get(cv.CAP_PROP_FRAME_HEIGHT))  # width by height
# window_size = 1280, 720
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Flappy Bird')

# sound effect
pygame.mixer.music.load('./FlappyBirdResources/FlappyBirdThemeSong.mp3')
pygame.mixer.music.play(-1)

# Bird and pipe init
bird_img = pygame.image.load("./FlappyBirdResources/bird_sprite.png")
bird_img = pygame.transform.scale(bird_img, (bird_img.get_width() / 6, bird_img.get_height() / 6))
bird_frame = bird_img.get_rect()
bird_frame.center = (window_size[0] // 6, window_size[1] // 2)
pipe_frames = deque()
pipe_img = pygame.image.load("./FlappyBirdResources/pipe_sprite_single.png")

pipe_starting_template = pipe_img.get_rect()
space_between_pipes = 250

# Game loop
game_clock = time.time()
stage = 1
pipeSpawnTimer = 0
time_between_pipe_spawn = 40
dist_between_pipes = 500
pipe_velocity = lambda: dist_between_pipes / time_between_pipe_spawn
level = 0
score = 0
didUpdateScore = False
game_is_running = True

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while True:

        # Check if game is running
        if not game_is_running:
            text = pygame.font.SysFont("Helvetica Bold.ttf", 64).render('Game over!', True, (99, 245, 255))
            tr = text.get_rect()
            tr.center = (window_size[0] / 2, window_size[1] / 2)
            screen.blit(text, tr)

            # game over thing
            img = imgGameOver
            cv.putText(img, str(score).zfill(2), (585, 380), cv.FONT_HERSHEY_COMPLEX, 2.5,
                        (200, 0, 200), 5)

            pygame.display.update()
            pygame.time.wait(2000)
            VID_CAP.release()
            cv.destroyAllWindows()
            pygame.quit()
            sys.exit()

        # Check if user quit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                VID_CAP.release()
                cv.destroyAllWindows()
                pygame.quit()
                sys.exit()

        # Get frame
        ret, frame = VID_CAP.read()

        if not ret:
            print("Empty frame, continuing...")
            continue

        # Clear screen
        screen.fill((125, 220, 232))

        # Face mesh
        frame.flags.writeable = False
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = face_mesh.process(frame)
        frame.flags.writeable = True

        # Draw mesh
        if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
            # 94 = Tip of nose
            marker = results.multi_face_landmarks[0].landmark[94].y
            bird_frame.centery = (marker - 0.5) * 1.5 * window_size[1] + window_size[1] / 2
            if bird_frame.top < 0:
                bird_frame.y = 0
            if bird_frame.bottom > window_size[1]:
                bird_frame.y = window_size[1] - bird_frame.height

        # A background thing
        frame = cv.addWeighted(frame, 0.2, imgBackground, 0.8, 0)
        # Mirror frame, swap axes because opencv != pygame
        frame = cv.flip(frame, 1).swapaxes(0, 1)

        # Update pipe positions
        for pf in pipe_frames:
            pf[0].x -= pipe_velocity()
            pf[1].x -= pipe_velocity()

        if len(pipe_frames) > 0 and pipe_frames[0][0].right < 0:
            pipe_frames.popleft()

        # Update screen
        # opencv frame in pygame screen
        pygame.surfarray.blit_array(screen, frame)
        screen.blit(bird_img, bird_frame)
        checker = True
        for pf in pipe_frames:
            # Check if bird went through to update score
            if pf[0].left <= bird_frame.x <= pf[0].right:
                checker = False
                if not didUpdateScore:
                    score += 1
                    didUpdateScore = True
            # Update screen
            screen.blit(pipe_img, pf[1])
            screen.blit(pygame.transform.flip(pipe_img, 0, 1), pf[0])
        if checker:
            didUpdateScore = False

        # Stage, score text
        text = pygame.font.SysFont("Helvetica Bold.ttf", 50).render(f'Stage {stage}', True, (99, 245, 255))
        tr = text.get_rect()
        tr.center = (100, 50)
        screen.blit(text, tr)
        text = pygame.font.SysFont("Helvetica Bold.ttf", 50).render(f'Score: {score}', True, (99, 245, 255))
        tr = text.get_rect()
        tr.center = (100, 100)
        screen.blit(text, tr)

        # Update screen
        pygame.display.flip()

        # Check if bird is touching a pipe
        if any([bird_frame.colliderect(pf[0]) or bird_frame.colliderect(pf[1]) for pf in pipe_frames]):
            game_is_running = False

        # Time to add new pipes
        if pipeSpawnTimer == 0:
            top = pipe_starting_template.copy()
            # top.x, top.y = window_size[0], random.randint((120 - 1000), (window_size[1] - 120 - space_between_pipes - 1000))
            top.x = window_size[0]
            a = 120 - 1000
            b = window_size[1] - 120 - space_between_pipes - 800
            top.y = random.randint(a, b)
            bottom = pipe_starting_template.copy()
            bottom.x, bottom.y = window_size[0], top.y + 1000 + space_between_pipes
            pipe_frames.append([top, bottom])

        # Update pipe spawn timer - make it cyclical
        pipeSpawnTimer += 1
        if pipeSpawnTimer >= time_between_pipe_spawn:
            pipeSpawnTimer = 0

        # Update stage
        if time.time() - game_clock >= 10:
            time_between_pipe_spawn *= 5 / 6
            stage += 1
            game_clock = time.time()
