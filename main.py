import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
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
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()