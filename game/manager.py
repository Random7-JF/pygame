import pygame
from object.player import *

class Manager():
    def __init__(self):
        self.draw_group = pygame.sprite.Group()
        self.update_group = pygame.sprite.Group()
        self.spawn_player()
    
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
        self.player = Player(150,150)
        self.add_group_to_draw(self.player)
        self.add_group_to_update(self.player)
