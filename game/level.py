import csv
import pygame
class Level():
    def __init__(self, level) -> None:
        self.level = level
        self.level_coords =  []
    
    def load_level(self):
        level_file = "game/levels/" + self.level + ".csv"
        with open(level_file, "r") as levelfile:
            reader = csv.reader(levelfile)
            for line in reader:
                coord = pygame.Vector2()
                coord.x = int(line[0])
                coord.y = int(line[1])
                self.level_coords.append(coord)