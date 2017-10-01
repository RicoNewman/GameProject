import pygame, sys, random
from pygame.locals import *

def Text(T): #handy for setting text on the screen, pass any text argument
	windowSurface.fill(BLACK)
	basicFont = pygame.font.SysFont(None, 30)
	text = basicFont.render(T,True, WHITE) 
	textRect = text.get_rect() 
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery
	windowSurface.blit(text, textRect)
	return True
def GameOver (x): #can use this later, allows the game to be reset
	basicFont = pygame.font.SysFont(None, 30)
	text = basicFont.render("Game Over", True, WHITE)
	text2 = basicFont.render("You hit the " + x, True, WHITE) 
	textRect = text.get_rect() 
	text2Rect = text2.get_rect() 
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery
	text2Rect.centerx = windowSurface.get_rect().centerx
	text2Rect.centery = windowSurface.get_rect().centery
	text2Rect.top += 50
	windowSurface.blit(text, textRect)
	windowSurface.blit(text2, text2Rect)
	return True
def DirectionAddedX(x, y, z): #dont need this yet
	global segments
	if y == 0:
		if x == 8:
			Value = player.left
		if x == 2:
			Value = player.left
		if x == 4:
			Value = player.right+PLAYER
		if x == 6:
			Value = player.left - 2*PLAYER
	else:
		if z == 8:
			Value = segments[y-1].left
		if z == 2:
			Value = segments[y-1].left
		if z == 4:
			Value = segments[y-1].right
		if z == 6:
			Value = segments[y-1].left - PLAYER
	return Value
def rot_centre(image,angle):
    windowSurface.fill(BLACK)
    rot_sprite=pygame.transform.rotate(image,angle)
    playerBox=rot_sprite.get_rect()
    playerBox.centerx=200
    playerBox.centery=600
    windowSurface.blit(rot_sprite, playerBox)
    pygame.display.update()
    return rot_sprite

#set up 
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Input')

BLACK =(0, 0, 0,)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#set up the player and food data structure
PLAYER = 200
MOVESPEED = 20
ANGLESTEP = 5
State = False
Pause =False
playerBox = pygame.Rect(0,WINDOWHEIGHT/2,PLAYER,PLAYER)
#foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))
moveUp = False
moveDown = False
Yes=True
Rotator = pygame.image.load('CannonBarrel.png')
Rotator = pygame.transform.scale(Rotator, (PLAYER, PLAYER))
pygame.display.update()
angle=-5
while True:
    while State ==False and Pause == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: #change the keydown (Keys pressed down) variables
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                    if angle <= 40:
                        angle+=ANGLESTEP
                        finCannon =rot_centre(Rotator, angle)
                    print(angle)
                
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
                    print(angle)
                    if angle >= -20:
                        angle-=ANGLESTEP
                        finCannon=rot_centre(Rotator, angle)

