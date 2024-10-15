import pygame
from game.constants import * 

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.width = LEVEL_BLOCK_WIDTH
        self.height = LEVEL_BLOCK_HEIGHT

    def draw(self, screen):
        xpos = self.position.x - self.width
        ypos = self.position.y - self.height
        pygame.draw.rect(screen, "white", pygame.Rect(xpos, ypos, self.width, self.height), 4) 


    def update(self, screen):
        pass 