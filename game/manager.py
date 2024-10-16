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

        # I want to load a map in here.
        block = Block(400, 400)
        block2 = Block(900, 400)
        block3 = Block(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.add_group_to_draw(block)
        self.add_group_to_update(block)
        self.add_group_to_draw(block2)
        self.add_group_to_update(block2)
        self.add_group_to_draw(block3)
        self.add_group_to_update(block3)