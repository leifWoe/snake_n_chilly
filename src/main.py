import pygame, sys, random
from pygame.math import Vector2

# creating a grid (kinda)
class SNAKE:
    def __init__(self) -> None:
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        
    # draw every part of snake     
    def draw_snake(self):
        for part in self.body:
            #draw a rect for every body part (self.body entrys)
            snake_rect = pygame.Rect(int(part.x * cell_size),int(part.y * cell_size),cell_size,cell_size) # vector float to int
            #draw them
            pygame.draw.rect(screen,(0,0,0),snake_rect)
                    
class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_count - 1) # random placements for x (for 0 till cell_count-1, too make sure it is always completly inside of the window)
        self.y = random.randint(0,cell_count - 1) # random placements for x (for 0 till cell_count-1, too make sure it is always completly inside of the window)
        self.pos = Vector2(self.x,self.y) # create x n y pos inside a Vectore
        
    # draw the fruit on board
    def draw_fruit(self):
        #create it (x * cell_size,y * cell_size,w,h) // vector float to int
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        #draw it (main surface,color (RGB Tuple) ,rectangle(fruit_rect))
        pygame.draw.rect(screen,(126,166,114),fruit_rect)


pygame.init()
pygame.display.set_caption("Snake and chilly") #name of the window
cell_size = 40
cell_count = 20
window_resolution = (cell_size*cell_count, cell_size*cell_count) #window size
running = True

screen = pygame.display.set_mode(window_resolution)
clock = pygame.time.Clock() 

fruit = FRUIT()
snake = SNAKE()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(('blue'))      
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60) #60 frames max per sec
