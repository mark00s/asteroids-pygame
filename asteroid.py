import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = self.velocity.rotate(random_angle) * 1.2  # Faster!
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = self.velocity.rotate(-random_angle)
