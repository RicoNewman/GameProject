import pygame, sys, random
from pygame.locals import *

def Text(T):
	windowSurface.fill(BLACK)
	basicFont = pygame.font.SysFont(None, 30)
	text = basicFont.render(T,True, WHITE) 
	textRect = text.get_rect() 
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery
	windowSurface.blit(text, textRect)
	return True
def GameOver (x):
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
def DirectionAddedX(x, y, z):
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
def DirectionAddedY(x, y, z):
	if y == 0:
		if x == 8:
			Value = player.bottom + PLAYER
		if x == 2:
			Value = player.top - 2*PLAYER
		if x == 4:
			Value = player.top
		if x == 6:
			Value = player.top
	else:
		if z == 8:
			Value = segments[y-1].bottom
		if z == 2:
			Value = segments[y-1].top - PLAYER
		if z == 4:
			Value = segments[y-1].top
		if z == 6:
			Value = segments[y-1].top
	
	return Value

#set up 
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Input')

BLACK =(0, 0, 0,)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#set up the player and food data structure
foodCounter = 0
NEWFOOD = 0
FOODSIZE = 20
PLAYER = 20
MOVESPEED = 20
State = False
Pause =False
player = pygame.Rect(WINDOWWIDTH/2,WINDOWHEIGHT/2,PLAYER,PLAYER)
foods = []
#foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))
	
#set up the movement variables
moveLeft =False
moveRight = False
moveUp = False
moveDown = False

Text('Pause with q')

while True:
	DIRECTION = 8
	moveLeft =False
	moveRight = False
	moveUp = False
	moveDown = False
	Snake = 0
	segments = []
	pDir = [8]
	while State == False and Pause == False:
		#check for the QUIT event
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
			
			if event.type == KEYDOWN:
				#change the keydown variables
				if event.key == K_LEFT or event.key == ord('a'):
					moveRight = False
					moveLeft = True
				if event.key == K_RIGHT or event.key == ord('d'):
					moveRight = True
					moveLeft = False		
				if event.key == K_UP or event.key == ord('w'):
					moveDown = False
					moveUp = True

				if event.key == K_DOWN or event.key == ord('s'):
					moveUp = False
					moveDown = True
			if event.type == KEYUP: # what happens when the key is released
				if event.key == ord('q'):
					MOVESPEED = 0
					print (segments)
				if event.key == K_LEFT or event.key == ord('a'):
					moveLeft = False
				if event.key == K_RIGHT or event.key == ord('d'):
					moveRight =False
				if event.key == K_UP or event.key == ord('w'):
					moveUp = False	
				if event.key == K_DOWN or event.key == ord('s'):
					moveDown = False
				if event.key == ord('e'):
					MOVESPEED = 20
					
		if len(foods) <= NEWFOOD:
			#add new food
			#foodCounter = 0
			foods.append(pygame.Rect(random.randint(0, WINDOWHEIGHT-FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))
			
		#draw the black background onto the surface
		windowSurface.fill(BLACK)
		
		
		# move the player		
		if moveDown:# and player.bottom < WINDOWHEIGHT:
			DIRECTION = 2
		if moveUp:# and player.top > 0:
			DIRECTION = 8
		if moveRight:# and player.right < WINDOWWIDTH:
			DIRECTION = 6
		if moveLeft:# and player.left > 0:
			DIRECTION = 4
			
		if DIRECTION == 2:# and pDir[1]!=8: #and player.bottom < WINDOWHEIGHT:
			pDir.insert(0,DIRECTION)
			player.top += MOVESPEED
		if DIRECTION == 8:#  and pDir[1]!=2: #:and player.top > 0
			player.top -= MOVESPEED
			pDir.insert(0,DIRECTION)
		if DIRECTION == 6:#  and pDir[1]!=4: #and player.right < WINDOWWIDTH:
			player.right += MOVESPEED
			pDir.insert(0,DIRECTION)
		if DIRECTION == 4:# and pDir[1]!=6: #and player.left > 0 
			player.left -= MOVESPEED
			pDir.insert(0,DIRECTION)
		if segments !=[]:
			if DIRECTION == 2 and pDir[1]==8 or DIRECTION == 4 and pDir[1]==6 or  DIRECTION == 8 and pDir[1]==2 or DIRECTION == 6 and pDir[1]==4:
				State = GameOver("yourself")
			
		#stop run off/game over
		#if DIRECTION == pDir:
			#State = GameOver("bottom")
		if player.bottom> WINDOWHEIGHT:
			State = GameOver("bottom")
		if player.left > WINDOWWIDTH-PLAYER+1:
			State = GameOver("right")
		if player.left < 0:
			State = GameOver("left")
		if player.top < 0:
			State = GameOver("top")
		
		# draw the player onto the surface
		pygame.draw.rect(windowSurface, RED, player)
		
		#check if the player has intersected with any food squares
		for food in foods[:]:
			if player.colliderect(food): # a preprogrammed collide checker
				foods.remove(food)
				#add new segment
				segments.append(pygame.Rect(DirectionAddedX(DIRECTION, len(segments), pDir[len(segments)-1]), DirectionAddedY(DIRECTION, len(segments),pDir[len(segments)] ), PLAYER, PLAYER))
				
				
					
		for i in range(len(segments)):
			if pDir[i+1] == 8:
				segments[i].top -= MOVESPEED 
			if pDir[i+1] == 2:
				segments[i].top += MOVESPEED 
			if pDir[i+1] == 6:
				segments[i].left += MOVESPEED 
			if pDir[i+1] == 4:
				segments[i].left -= MOVESPEED  
		for segment in segments:	
			if player.colliderect(segment):
				State = GameOver("yourself")
		#draw the food
		for i in range(len(foods)):
			pygame.draw.rect(windowSurface, GREEN, foods[i])
		#draw the segments	
		for i in range(len(segments)):
			segment = pygame.draw.rect(windowSurface, WHITE, segments[i])
			basicFont = pygame.font.SysFont(None, 20)
			number = basicFont.render(str(i+1),True, RED) 
			windowSurface.blit(number, segment)
		
		print (pDir)
		#draw the window onto the screen
		pygame.display.update()
		mainClock.tick(10)
	#after game ends
	segments = []
	mainClock.tick(1)
	player.top = 200
	player.left =200
	DIRECTION = 8
	Text("Press w to Restart")
	pygame.display.update()
	State = True 
	for event in pygame.event.get():
		if event.type == QUIT :
				pygame.quit()
				sys.exit()
		if event.type == KEYUP: 
			if event.key == ord('w'):
				DIRECTION = 8
				State = False
			
		else: 
			Text("Press w to Restart")
			pygame.display.update()