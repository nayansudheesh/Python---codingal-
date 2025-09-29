import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprites moving')
RED = (139,0,0)
x = 0
y = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
     y = y - 1 
    if pressed[pygame.K_DOWN]:
     y = y + 1
    if pressed[pygame.K_RIGHT]:
     x = x + 1
    if pressed[pygame.K_LEFT]:
     x = x - 1
    screen.fill((0, 0, 0))  
    pygame.draw.rect(screen ,RED, pygame.Rect(400, 5 , 200, 100)) 
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 60, 60)) 
    pygame.display.flip()