import pygame

pygame.init()
screen = pygame.display.set_mode((400, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.set_caption("Snake and chilly")            
    pygame.display.update()            