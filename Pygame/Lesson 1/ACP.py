import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my first game screen")
grey = (58,58,58)
tree_image = pygame.transform.scale(pygame.image.load("Lesson 1/Tree.PNG").convert_alpha(), (300 , 300))
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.fill(grey)
    window.blit(tree_image, (0,0))
    pygame.display.flip()