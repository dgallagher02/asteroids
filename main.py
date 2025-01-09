import pygame
from constants import *
from player import *
from circleshape import CircleShape
import sys
from asteroid import *
from asteroidfield import AsteroidField

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateble, drawable)
    Asteroid.containers = (asteroids, updateble, drawable)
    AsteroidField.containers = (updateble)
    Shot.containers = (shots, updateble, drawable)

    guy = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

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
        for asteroid in asteroids:
            if asteroid.collision(guy):
                print("Game over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()