import pygame
from pygame.locals import *

import math
import cv2

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minecraft Compass")

def userinput():
    font = pygame.font.font.SysFont("comicsansms", 72)
    text = font.render("Enter the direction you want to go", True, (0, 0, 0))
    return screen.blit(text, (10, 10))

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
        compass = pygame.image.load("untitled.png").convert()
        compass = pygame.transform.scale(compass, (100, 100))
        screen.blit(compass, (400, 250))

        # get needle to point to the mouse
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        # get the angle of the needle
        angle = math.degrees(math.atan2(mouse_y , mouse_x))
        print(angle)


        # rotate the needle
        compass = pygame.transform.rotate(compass, angle)

        # post the compass image into the screen at center
        screen.blit(compass, (400, 250))



        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
        

    

if __name__ == "__main__":
    main()
