from cProfile import run
from re import X
from turtle import width

from sqlalchemy import true
import pygame
import math
pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulador de Planetas")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU #1AU = 100 pixeles
    TIMESTEP = 3600 * 24 # 1 dia

    def _init_(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + width / 2
        y = self.y * self.SCALE + height / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

def main():
    run = true
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)

    planets = [sun, earth]

    while run:
        clock.tick(60)
        #win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.draw(win)

        pygame.display.update()

    pygame.quit()

main()