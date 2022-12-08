import pygame, sys, random
from pygame.math import Vector2
 
# creating a grid (kinda)
class SNAKE:
    #method to intit n create snake with starting pos
    #todo adding random starting pos 
    def __init__(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(1,0) # only right movement
        self.new_part = False #allowing only one part to bet added // no new elements allowed for move_snake() at the beginning of the game
        
    # method to draw every part of snake     
    def draw_snake(self):
        for part in self.body:
            #draw a rect for every body part (self.body entrys)
            snake_rect = pygame.Rect(int(part.x * cell_size),int(part.y * cell_size),cell_size,cell_size) # vector float to int
            #draw them
            pygame.draw.rect(screen,(255,255,255),snake_rect)
    
    #method to move the snake every 150 milli sec's [timer]
    #the head ist moved to a ne block [dircetion input]
    #each block afterwards is moved to the block that used to be before it
    #than deleteing last block and coping the list, ready for a new input 
           
    def move_snake(self):
        if self.new_part == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction) #inserting a the first pos of body list a new part with direction vector added
            self.body = body_copy[:] #copying new list into self.body attribut
            self.new_part = False
        else:
            body_copy = self.body[:-1] #deleting last entry in body list
            body_copy.insert(0,body_copy[0] + self.direction) #inserting a the first pos of body list a new part with direction vector added
            self.body = body_copy[:] #copying new list into self.body attribut
        
    def add_part(self):
        self.new_part = True #allow now that fruit and snake head are on same pos -> new part
class FRUIT:
    def __init__(self):
        self.randomize()# place fruit at random place at start of game 
        
    # draw the fruit on board
    def draw_fruit(self):
        #create it (x * cell_size,y * cell_size,w,h) // vector float to int
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        #draw it (main surface,color (RGB Tuple) ,rectangle(fruit_rect))
        pygame.draw.rect(screen,(237,148,77),fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0,cell_count - 1) # random placements for x (for 0 till cell_count-1, too make sure it is always completly inside of the window)
        self.y = random.randint(0,cell_count - 1) # random placements for x (for 0 till cell_count-1, too make sure it is always completly inside of the window)
        self.pos = Vector2(self.x,self.y) # create x n y pos inside a Vectore
        
class MAIN: #game class to clean up game loop and can check relation
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self): #update game, move snake and check for collision between snake n fruit / game over statements
        self.snake.move_snake()
        self.check_food()
        self.check_over()
        
    def draw(self): #create snake / draw it 
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_food(self): #check for collision
        if self.fruit.pos == self.snake.body[0]:
            #reposition fruit
            self.fruit.randomize()
            #add part to snake
            self.snake.add_part()
            #check if true 
            print('snack')
    
    def check_over(self):
        #check hit wall
        if not 0 <= self.snake.body[0].x < cell_count or not 0 <= self.snake.body[0].y < cell_count: #game has 19 tiles so < cell_count
            print('fail')
        #check if snake hits itself
        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                print('fail')

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
pygame.display.set_caption("Snake and chilly") #name of the window
cell_size = 40
cell_count = 20
window_resolution = (cell_size*cell_count, cell_size*cell_count) #window size
running = True

screen = pygame.display.set_mode(window_resolution)
clock = pygame.time.Clock() 

#[event timer] every 150 milli sec's
SCREEN_UPDATE = pygame.USEREVENT #event capitalised in pygame by convention 
pygame.time.set_timer(SCREEN_UPDATE,150) 

main_game = MAIN()

#[event loop]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quiting game and stop running it
            pygame.quit()
            sys.exit()
        #always move the snake, every 150 milli sec's    
        if event.type == SCREEN_UPDATE:
            main_game.update()
        #[direct input]
        if event.type == pygame.KEYDOWN:
            #UP
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1: #if snake moves downwards (direction y = 1) -> cant move straight upwards
                    main_game.snake.direction = Vector2(0,-1)
            #DOWN    
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            #RIGHT   
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
            #LEFT
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)

    screen.fill((164,180,140))
    main_game.draw()
    pygame.display.update()
    clock.tick(60) #60 frames max per sec