import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Player.containers = (drawables, updatables)
    Shot.containers = (drawables, shots, updatables)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Exit on Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.kill()
                    shot.kill()

        screen.fill((0, 0, 0))
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000  # ms


if __name__ == "__main__":
    main()
