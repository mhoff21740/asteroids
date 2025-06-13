# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame


#import constant variables from constants.py into main.py
from constants import * 
from circleshape import *
from player import *
from asteroidfield import *


def main():
    pygame.init() # initializes the pygame library
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock() # set the frame rate to 60 frames per second
dt = 0


asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

AsteroidField.containers = (updatable)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)


player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        # exit the game if the window is closed
    pygame.Surface.fill(screen, (0,0,0))  # fill the screen with black color
    updatable.update(dt)
    for asteroid in asteroids:
        if asteroid.collision(player):
            print("Game Over!")
            pygame.quit()
            raise SystemExit 
    for player in drawable:
        player.draw(screen)
    pygame.display.flip()
    
   
   
   
   
   
   
    # this creates a window with the specified width and height
    dt = clock.tick(60) / 1000.0
        






if __name__ == "__main__":
    main()
    # this initializes the pygame library