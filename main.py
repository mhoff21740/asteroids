# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame


#import constant variables from constants.py into main.py
from constants import * 


def main():
    pygame.init() # initializes the pygame library
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        # exit the game if the window is closed
        pygame.Surface.fill(screen, (0,0,0))  # fill the screen with black color
        pygame.display.flip()
        # this creates a window with the specified width and height






if __name__ == "__main__":
    main()
    # this initializes the pygame library