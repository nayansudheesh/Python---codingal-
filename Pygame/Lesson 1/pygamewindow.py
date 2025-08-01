import pygame

pygame.init() #initialising

screen = pygame.display.set_mode((400,500))
#create a loop to run untill game is quit by user
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.display.flip() #making changes visible
