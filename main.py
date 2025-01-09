import pygame
from constants import *
from player import *
from circleshape import CircleShape
import sys

print(f"Python version: {sys.version}")
print(f"Pygame version: {pygame.version.ver}")
print(f"Running from: {sys.executable}")

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateble, drawable)

    guy = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        color = (0,0,0)
        screen.fill("black")
        # guy.update(dt)
        # guy.draw(screen)
        for thing in updateble:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()