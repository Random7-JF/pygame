import pygame
from object.player import *
from object.block import *
from game.constants import *
from game.level import *

class Manager():
    def __init__(self):
        self.draw_group = pygame.sprite.Group()
        self.update_group = pygame.sprite.Group()
        self.spawn_player()
        self.spawn_level()
    
    # Add function to add object group to Draw calls
    def add_group_to_draw(self, object):
        self.draw_group.add(object)

    # Add function to add object group to Update calls
    def add_group_to_update(self, object):
        self.update_group.add(object)
    
    ##Add function to add object to object group
    ##Remove Object from object group
    ##Remove Object group from groups
    def spawn_player(self):
        self.player = Player(SCREEN_HEIGHT * 0.95, SCREEN_WIDTH / 2)
        self.add_group_to_draw(self.player)
        self.add_group_to_update(self.player)

    def spawn_level(self):
        level = Level("level1")
        level.load_level()

        for block in level.level_coords:
            new_block = Block(block[0], block[1])
            self.add_group_to_draw(new_block)
            self.add_group_to_update(new_block)