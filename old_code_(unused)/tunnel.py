import pygame
from pygame.locals import *
import random
import math
import time


class Run3Model:
    """docstring coming soon"""

    def __init__(self):
        self.number_of_lives = 3
        self.pit = Pit(
            300,
            100,
            200,
            20,
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        )
        self.runner = Runner(200, 450, 100, 20)

    def update(self):
        self.runner.update()
        self.pit.update()


class Pit:
    """docstring coming soon"""

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vy = 0.0
        self.scaler = 0.0

    def update(self):
        self.y += self.vy
        self.width += self.scaler
        self.height += self.scaler


class Runner:
    """docstring coming soon"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.vx = 0.0

    def update(self):
        self.x += self.vx


class Run3View:
    """docstring coming soon"""

    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        pygame.draw.rect(
            self.screen,
            pygame.Color(
                self.model.pit.color[0],
                self.model.pit.color[1],
                self.model.pit.color[2],
            ),
            pygame.Rect(
                self.model.pit.x,
                self.model.pit.y,
                self.model.pit.width,
                self.model.pit.height,
            ),
        )
        pygame.draw.rect(
            self.screen,
            pygame.Color(
                self.model.runner.color[0],
                self.model.runner.color[1],
                self.model.runner.color[2],
            ),
            pygame.Rect(
                self.model.runner.x,
                self.model.runner.y,
                self.model.runner.width,
                self.model.runner.height,
            ),
        )
        pygame.display.update()


class PyGameKeyboardController:
    """docstring coming soon"""

    def __init__(self, model):
        self.model = model

    def handle_pygame_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.runner.vx += -1.0
        if event.key == pygame.K_RIGHT:
            self.model.runner.vx += 1.0
        if event.key == pygame.K_DOWN:
            self.model.pit.vy += 0.5
            self.model.pit.scaler += 0.5


if __name__ == "__main__":
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    model = Run3Model()
    view = Run3View(model, screen)
    controller = PyGameKeyboardController(model)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)
        model.update()
        view.draw()
        time.sleep(0.001)

    pygame.quit()
