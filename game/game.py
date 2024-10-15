import pygame
from game.constants import *

class Game():
    def __init__(self):
        self.delta_time = 0.0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def spawn_manager():
        pass
    
    def run(self):
        while True:
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            # Iterate over Object groups and call update
            # Iterate over Object groups and call draw
        
            pygame.display.flip()
            self.delta_time = (self.clock.tick(60) / 1000)

    ##Add function to add object group to Draw calls
    def add_group_to_draw(self, group):
        pass
    ##Add function to add object group to Update calls
    def add_group_to_update(self, group):
        pass
    ##Add function to add object to object group
    ##Remove Object from object group
    ##Remove Object group from groups