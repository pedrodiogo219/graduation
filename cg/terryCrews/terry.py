import pygame
from pygame.locals import *

#INIT
pygame.init()


# EVENT
def LeftClick():
	return event.type == MOUSEBUTTONDOWN and event.button == 1

def RightClick():
	return event.type == MOUSEBUTTONDOWN and event.button == 3

def MouseCoord():
	return pygame.mouse.get_pos()

def Inside(rect):
	return rect.left <= pygame.mouse.get_pos()[0] <= rect.right and rect.top <= pygame.mouse.get_pos()[1] <= rect.bottom


# SCREEN
width = 600
height = 600
screen = pygame.display.set_mode((width, height))


# PICTURES
# icon = pygame.image.load('pictures/icon.png')

orc = pygame.image.load('Pictures/orc.png')
orc = pygame.transform.scale(orc, (115, 150))
orc_rect = orc.get_rect()
orc_rect.move_ip(230,0)

mage = pygame.image.load('Pictures/mage.png')
mage = pygame.transform.scale(mage, (115, 150))
mage_rect = mage.get_rect()
mage_rect.move_ip(0,0)

warrior = pygame.image.load('Pictures/warrior.png')
warrior = pygame.transform.scale(warrior, (115, 150))
warrior_rect = warrior.get_rect()
mage_rect.move_ip(115,0)

# pygame.display.set_icon(icon)

# LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if LeftClick():
        	print("Left")

        if RightClick():
        	print("Right")

        if event.type == MOUSEMOTION:
        	print(pygame.mouse.get_pos())

        	if Inside(orc_rect):
           		print("Orc Terry Select")

        	if  Inside(warrior_rect):
        		print("Warrior Terry Select")

        	if Inside(mage_rect):
        		print("Mage Terry Select")


    screen.blit(mage, mage_rect)
    screen.blit(warrior, warrior_rect)
    screen.blit(orc, orc_rect)
    pygame.display.update()
