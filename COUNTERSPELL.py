import pygame
import random
import time

pygame.init()

#basiiiiiiiic
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("prototype")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

gggrr = pygame.image.load(r"C:\Users\vina\Documents\Computing\counter\bookenemy.jpg").convert()
gggrr = pygame.transform.scale(gggrr, (160, 210))

backgroundA = pygame.image.load(r"C:\Users\vina\Documents\Computing\counter\backgrounda.jpg").convert()
backgroundA = pygame.transform.scale(backgroundA, (SCREEN_WIDTH, SCREEN_HEIGHT))
background="A"

backgroundB = pygame.image.load(r"C:\Users\vina\Documents\Computing\counter\backgroundb.jpg").convert()
backgroundB = pygame.transform.scale(backgroundB, (SCREEN_WIDTH, SCREEN_HEIGHT))


#player is
player_width = 160
player_height = 200
player_x = SCREEN_WIDTH // 4
player_y = SCREEN_HEIGHT- player_height - 73    #x,y
player_speed = 7
player_jumpspeed = -10
acceleration=1
velocity_y=0
on_ground=True

#player mobvement running
game = True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game = False

            
 #player get controls
    key=pygame.key.get_pressed()
    if key[pygame.K_a]:
        player_x -= player_speed
    if key[pygame.K_d]:
        player_x += player_speed
    if key[pygame.K_w]:
        player_y += player_jumpspeed
        

    #stay in screen
    if player_x<0:
         player_x=0
    if player_x>SCREEN_WIDTH: ##########
        background='B' #########################
        player_x=0

    #jump
    if key[pygame.K_w] and on_ground:
        velocity_y=player_jumpspeed
        on_ground=False

        
    velocity_y+=acceleration #get pos
    player_y+=velocity_y #position due to jump and gravity

    if player_y >= SCREEN_HEIGHT-player_height- 73:
        player_y = SCREEN_HEIGHT - player_height - 73
        velocity_y=0
  
        on_ground=True
        


    #draw

    screen.fill(WHITE)

    if player_x>=SCREEN_WIDTH+player_width and background==B'':
            player_x=SCREEN_WIDTH

    if background=='A':
        screen.blit(backgroundA, (0,0)) #image
    elif background=='B':
        screen.blit(backgroundB, (0,0)) #image2
        pygame.draw.rect(screen, RED, (328,380, 83,57))
        escape=False
        if player_x>50:
            escape=True

    
    
    pygame.draw.rect(screen, RED, (player_x, player_y,player_width, player_height))
    screen.blit(gggrr, (player_x, player_y,player_width, player_height))

    
    pygame.display.flip() #updates the displya
    pygame.time.Clock().tick(60) #60 fps

##if escape==True and player_x==0:
    


#######################END
pygame.quit()
