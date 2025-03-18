import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
            for asteroid in asteroids:
                if asteroid.collision(player):
                    print("Game Over!")
                    sys.exit()
                for bullet in shots:
                    if bullet.collision(asteroid):
                        bullet.kill()
                        asteroid.split(screen)
            

            
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
         



if __name__ == "__main__":
    main()