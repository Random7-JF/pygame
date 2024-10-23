import pygame
from game.constants import * 

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        super().__init__()
        self.radius = radius
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2()
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)
    
    def update(self, delta_time):
        self.velocity.y = BALL_SPEED * delta_time
        self.position.y += self.velocity.y