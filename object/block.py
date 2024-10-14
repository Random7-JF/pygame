import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        #pygame.draw.polygon(screen,"white",[(100,100),(300,100), (300, 200),(100,200)], 4)
        pass

    def update(self, screen):
        pass 