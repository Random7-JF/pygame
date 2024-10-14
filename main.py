import pygame
from game.constants import *
from object.block import *
from object.player import *

def main():
    delta_time = 0.0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.90)

    # Main Game Loop
    while True:
        screen.fill("black")
        player.update(delta_time)
        player.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        delta_time = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()