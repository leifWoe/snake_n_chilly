import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
    pygame.display.set_caption("Snake and chilly")            
    pygame.display.update()