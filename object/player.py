import pygame
from object.block import *
from game.constants import *

class Player(Block):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.colour = "blue"
        self.height = 25
        self.width = 150
        self.move_speed = PLAYER_MOVE_SPEED
    
    def draw(self, screen) -> None:
        xpos = self.position.x - self.width
        ypos = self.position.y - self.height
       # print("(x,y)", self.position, "width:", self.width, "height:", self.height, "xpos:", xpos, "ypos:", ypos)
        pygame.draw.rect(screen, self.colour, pygame.Rect(xpos, ypos, self.width, self.height), 4) 

    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.position.x = self.position.x - self.move_speed * delta_time
        if keys[pygame.K_d]:
            self.position.x = self.position.x + self.move_speed * delta_time
