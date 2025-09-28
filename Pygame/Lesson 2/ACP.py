import pygame

pygame.init()
def main():
    pygame.init()
    screen_width, screen_height = 650, 480
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('my first game screen')
main()
WHITE = (255,255,255)
pygame.draw.rect(screen,WHITE, pygame.Rect(60,60,80,80), 0)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False