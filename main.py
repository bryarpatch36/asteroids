import pygame
from constants import *

def main():
    pygame.init()
    black = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(black)
        pygame.display.flip()



if __name__ == "__main__":
    main()