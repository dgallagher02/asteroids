import pygame
from constants import *

import sys
print(f"Python version: {sys.version}")
print(f"Pygame version: {pygame.version.ver}")
print(f"Running from: {sys.executable}")

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        color = (0,0,0)
        screen.fill("black")
        pygame.display.flip()
        pygame.time.delay(10)
    

if __name__ == "__main__":
    main()