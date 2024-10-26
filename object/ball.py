import pygame
import math
from game.constants import * 

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        super().__init__()
        self.radius = radius
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0.5,0.5)
        self.rotation = 60
        self.count = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)
    
    def update(self, delta_time):
        self.count += 1
        if self.count >= 10:
            self.rotation += 10 % 360
            self.count = 0
        rotation_to_radians = math.radians(self.rotation)
        self.velocity = pygame.Vector2(math.cos(rotation_to_radians), 
                                   math.sin(rotation_to_radians))
        self.position += self.velocity * BALL_SPEED * delta_time