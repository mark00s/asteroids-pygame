import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (drawables, updatables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Exit on Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatables:
            updatable.update(dt)

        screen.fill((0, 0, 0))
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000  # ms


if __name__ == "__main__":
    main()
