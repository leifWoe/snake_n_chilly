import pygame, sys, random
from pygame.math import Vector2
 
# creating a grid (kinda)
#todo add snake art
#todo adding diffrent colors for when has eaten more chillys
#todo game over menu // menu
#todo background update
#todo sound
class SNAKE:
    #method to intit n create snake with starting pos
    def __init__(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0) #no movement
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
        self.new_part = True #allow now that chilly and snake head are on same pos -> new part
        
    def reset(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0)
class CHILLY:
    def __init__(self):
        self.randomize()# place chilly at random place at start of game 
        
    # draw the chilly on board
    def draw_chilly(self):
        #create it (x * cell_size,y * cell_size,w,h) // vector float to int
        chilly_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        #draw chilly (surface(picture), placement)
        screen.blit(chilly,chilly_rect)        
        
        # OLD BLOCK DRWAING
        #draw it (main surface,color (RGB Tuple) ,rectangle(chilly_rect))
        #pygame.draw.rect(screen,(237,148,77),chilly_rect)
        
    def randomize(self):
        self.x = random.randint(0,cell_count - 1) # random placements for x (for 0 till cell_count-1, too make sure it is always completly inside of the window)
        self.y = random.randint(0,cell_count - 1) # random placements for x (for 0 till cell_count-1, too make sure it is always completly inside of the window)
        self.pos = Vector2(self.x,self.y) # create x n y pos inside a Vectore
        
class MAIN: #game class to clean up game loop and can check relation
    
    def __init__(self):
        self.snake = SNAKE()
        self.chilly = CHILLY()
        
    def update(self): #update game, move snake and check for collision between snake n chilly / game over statements
        self.snake.move_snake()
        self.check_food()
        self.check_over()
        
    def draw(self): #getter for chilly, snake, background // draw lasty what shoulb be on top 
        #self.draw_background()
        self.chilly.draw_chilly()
        self.snake.draw_snake()
        self.draw_score()
        
    def draw_background(self):
        darker_background_color = (155, 191, 114)
        for row in range(cell_count):
            if row % 2 == 1:
                for col in range(cell_count):
                    if col % 2 == 1:
                        background_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)#(x,y,w,h)
                        pygame.draw.rect(screen,darker_background_color,background_rect)
        
    def check_food(self): #check for collision
        if self.chilly.pos == self.snake.body[0]:
            #reposition chilly
            self.chilly.randomize()
            #add part to snake
            self.snake.add_part()
            #if true echo
            #print('snack')
            
            
            #if fruit on snake body randomize again
            for part in self.snake.body[1:]:
                if part == self.chilly.pos:
                    self.chilly.randomize()
    
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,12))#text, smooth text? True, color
        score_rect = score_surface.get_rect(center = (int(cell_size*cell_count-60),int(cell_size*cell_count-40))) #x,y // center where the locating rect places itself as reffrence to(x,y)
        chilly_score_rect = chilly.get_rect(midright = (score_rect.left,score_rect.centery)) #midright - mid right side of the rect gives place reffrence to be placed by// x = on left side of score rect //  y = socre height
        bg_rect = pygame.Rect(chilly_score_rect.left,chilly_score_rect.top,chilly_score_rect.width+5+score_rect.width,chilly_score_rect.height) #x,y,w,h
        
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
        screen.blit(score_surface,score_rect) #surface, position
        screen.blit(chilly,chilly_score_rect)
    
    def check_over(self):
        #check hit wall
        if not 0 <= self.snake.body[0].x < cell_count or not 0 <= self.snake.body[0].y < cell_count: #game has 19 tiles so < cell_count
            #print('fail')
            self.game_over()
        #check if snake hits itself
        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                #print('fail')
                self.game_over()

    def game_over(self):
        self.snake.reset()

pygame.init()
pygame.display.set_caption("Snake and chilly") #name of the window
cell_size = 40
cell_count = 20
window_resolution = (cell_size*cell_count, cell_size*cell_count) #window size
running = True

screen = pygame.display.set_mode(window_resolution)
clock = pygame.time.Clock() 

#game graphics
chilly = pygame.image.load('graphics/chilly.png').convert_alpha()
game_font = pygame.font.Font(None,25) #font , size

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
                if main_game.snake.direction.y != 1: #if snake moves downwards (direction y = 1) -> cant move straight upwards -> cant reverse snake
                    main_game.snake.direction = Vector2(0,-1)
            #DOWN    
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1: #cant reverse snake
                    main_game.snake.direction = Vector2(0,1)
            #RIGHT   
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            #LEFT
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

    screen.fill((164,180,140))
    main_game.draw() #draw collectivly eveything
    pygame.display.update()
    clock.tick(60) #60 frames max per sec