import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

sprite1 = pygame.Surface((100, 100))
sprite1_color = (255, 0, 0)
sprite1.fill(sprite1_color)
sprite1_rect = sprite1.get_rect(center=(200, 200))

sprite2 = pygame.Surface((100, 100))
sprite2_color = (0, 0, 255)
sprite2.fill(sprite2_color)
sprite2_rect = sprite2.get_rect(center=(400, 200))

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            sprite1_color = [random.randint(0, 255) for _ in range(3)]
            sprite2_color = [random.randint(0, 255) for _ in range(3)]
            sprite1.fill(sprite1_color)
            sprite2.fill(sprite2_color)

    screen.fill((30, 30, 30))
    screen.blit(sprite1, sprite1_rect)
    screen.blit(sprite2, sprite2_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()