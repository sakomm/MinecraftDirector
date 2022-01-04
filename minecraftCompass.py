import math

import pytesseract
import cv2

import pygame
from pygame.locals import *


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minecraft Compass")

def getCoordinates():
    #take a screenshot of the screen
    screenCap = cv2.VideoCapture(0)
    ret, img = screenCap.read()
    screenCap.release()

    #conver image to text without pytesseract
    text = 

    print(text)
    # x = int(x)
    # y = int(y)

    # #convert to radians
    # angle = math.atan2(y, x)
    # angle = math.degrees(angle)
    # angle = -1 * angle

    # #print coordinates
    # print("X: ", x)
    # print("Y: ", y)
    # print("Angle: ", angle)

    

def main():
    print("Starting Minecraft Compass")
    pygame.init()

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        screen.fill((255, 255, 255))

        #post the compass image into the screen at center
        compass = pygame.image.load("needle.jpg").convert()
        compass = pygame.transform.scale(compass, (100, 100))
        screen.blit(compass, (400, 250))

        # get needle to point to the mouse


        getCoordinates()
     
        angle = -1 * 35
        # rotate the needle around the center of the compass
        needle = pygame.transform.rotate(compass, angle)


        # post the compass image into the screen at center
        screen.blit(compass, (400, 250))



        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
        

    

if __name__ == "__main__":
    main()
