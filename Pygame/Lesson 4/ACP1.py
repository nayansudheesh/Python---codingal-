import math
import random
import pygame
from pygame import mixer

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
PLAYER_START_X, PLAYER_START_Y = 370, 380
ENEMY_START_Y_MIN, ENEMY_START_Y_MAX = 50, 150
ENEMY_SPEED_X, ENEMY_SPEED_Y = 4, 40
BULLET_SPEED_Y, COLLISION_DISTANCE = 12, 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

# Music (optional — remove if not available)
try:
    mixer.music.load('background.wav')
    mixer.music.play(-1)
except:
    pass

# Player
playerImg = pygame.image.load('player.png')
playerX, playerY = PLAYER_START_X, PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg, enemyX, enemyY, enemyX_change, enemyY_change = [], [], [], [], []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX, bulletY = 0, PLAYER_START_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score():
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (10, 10))

def player(x, y): screen.blit(playerImg, (x, y))
def enemy(x, y, i): screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    try:
        shoot_sound = mixer.Sound('laser.wav')
        shoot_sound.play()
    except:
        pass

def isCollision(ex, ey, bx, by):
    return math.hypot(ex - bx, ey - by) < COLLISION_DISTANCE

def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))
    again = font.render("Press R to Restart", True, (200, 200, 200))
    screen.blit(again, (270, 330))

# Game Loop
running, game_over = True, False
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: playerX_change = -5
                if event.key == pygame.K_RIGHT: playerX_change = 5
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Restart Game
                score_value = 0
                game_over = False
                enemyX = [random.randint(0, SCREEN_WIDTH - 64) for _ in range(num_of_enemies)]
                enemyY = [random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX) for _ in range(num_of_enemies)]
                bullet_state = "ready"
                bulletY = PLAYER_START_Y

    if not game_over:
        # Player
        playerX += playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

        # Enemies
        for i in range(num_of_enemies):
            if enemyY[i] > 340:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over = True
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                try:
                    explosion = mixer.Sound('explosion.wav')
                    explosion.play()
                except:
                    pass
                bulletY = PLAYER_START_Y
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= BULLET_SPEED_Y

        player(playerX, playerY)
        show_score()
    else:
        game_over_text()

    pygame.display.update()