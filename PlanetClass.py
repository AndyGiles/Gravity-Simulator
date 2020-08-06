import pygame
from random import random
from math import sin, cos, radians

def max(a, b): # returns the maximum of two numbers - used for finding the biggest planet
    if a.mass > b.mass:
        return a
    return b

class Planet:
    def __init__(self, mass, x, y, xv, yv):
        self.mass = mass
        self.radius = abs(mass ** (1 / 3))
        if self.radius < 1:  # makes sure all bodies are visible on the screen
            self.radius = 1
        self.color = (255, 255, 255)
        self.pos_x = x
        self.pos_y = y
        self.vel_x = xv
        self.vel_y = yv
        self.acc_x = 0
        self.acc_y = 0
        self.alive = True
        self.vectors = []
    def calculate(self, list, G):
        for planet in list:
            if planet.alive and not (self.pos_x == planet.pos_x and self.pos_y == planet.pos_y):
                magnitude = G * (self.mass * planet.mass) / ((planet.pos_x - self.pos_x) ** 2 + (planet.pos_y - self.pos_y) ** 2)  # strength of the force acting on the body
                x_vec = (planet.pos_x - self.pos_x) * magnitude
                y_vec = (planet.pos_y - self.pos_y) * magnitude
                self.vectors.append((x_vec, y_vec))
        self.acc_x = 0
        self.acc_y = 0
        for vector in self.vectors:  # accelerates the particle by every force vector that was calculated, (divided by its mass because a = F/m)
            self.acc_x += vector[0] / self.mass
            self.acc_y += vector[1] / self.mass
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y
        self.pos_x += self.vel_x  # moves each particle by its velocity every frame
        self.pos_y += self.vel_y
    def draw(self, screen, x, y, center_x, center_y):  # draws the particle on the screen - radius is proportional to the cube root of the mass (as if it was 3D)
        if self.alive:
            pygame.draw.circle(screen, self.color, (self.pos_x + x / 2 - center_x, self.pos_y + y / 2 - center_y), self.radius)
    def draw_vel(self, screen, x, y, center_x, center_y):  # draws a vector of the current velocity
        if self.alive:
            pygame.draw.line(screen, (0, 255, 0), (self.pos_x + x / 2 - center_x, self.pos_y + y / 2 - center_y), (self.vel_x * 5 + self.pos_x + x / 2 - center_x, self.vel_y * 5 + self.pos_y + y / 2 - center_y))
    def draw_acc(self, screen, x, y, center_x, center_y):  # draws a vector of the current acceleration
        if self.alive:
            pygame.draw.line(screen, (255, 255, 0), (self.pos_x + x / 2 - center_x, self.pos_y + y / 2 - center_y), (self.acc_x * 100 + self.pos_x + x / 2 - center_x, self.acc_y * 100 + self.pos_y + y / 2 - center_y))
    def distance(self, planet):  # returns the euclidean distance between self and another planet
        return ((self.pos_x - planet.pos_x) ** 2 + (self.pos_y - planet.pos_y) ** 2) ** 0.5
    def colliding(self, list):  # if the planet collides with another, it returns a Planet object of the othe planet, otherwise it returns False
        for planet in list:
            if self != planet and planet.alive:
                if self.distance(planet) <= self.radius + planet.radius:  # collision occurs when any part of any circle touches the other
                    return planet
        return False
