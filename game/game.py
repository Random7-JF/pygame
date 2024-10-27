import pygame
from game.constants import *
from game.manager import *

class Game():
    def __init__(self):
        self.delta_time = 0.0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.manager = Manager()
      
    def run(self):
        while True:
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            # Iterate over Object groups and call update
            for obj in self.manager.update_group:
                obj.update(self.delta_time)
            # Iterate over Object groups and call draw
            for obj in self.manager.draw_group:
                obj.draw(self.screen)
        
            pygame.display.flip()
            self.delta_time = (self.clock.tick(144) / 1000)

