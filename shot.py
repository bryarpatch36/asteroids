import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from player import *



class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, velocity)
        self.velocity = velocity
        self.radius = SHOT_RADIUS
        
# Draws the shot

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 0)
        
# Updates the postion of the shot in the direction of the player and sets the velocity.
    def update(self, dt):

        self.position += self.velocity * float(dt)