import csv

class Level():
    def __init__(self, level) -> None:
        self.level = level
        self.level_coords =  []
    
    def load_level(self):
        with open("game/levels/level1.csv", "r") as levelfile:
            reader = csv.reader(levelfile)
            for line in reader:
                print("Coord:", line)
                self.level_coords.append(line)
            print(self.level_coords)