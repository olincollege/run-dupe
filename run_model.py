"""_summary_"""

import random
import pygame
from run_view import AlienView, StartScreenView
from run_controller import (
    AlienController,
)
from run_start_screen import Button


class Game:
    """
    Runs the main game loop.

    Attributes:
        start_screen and run: Booleans that represent the state of the game.
    """

    def __init__(self):
        pygame.init()

        # Make mouse visible
        pygame.mouse.set_visible(True)

        # Create display window
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Set up start screen
        self.start_screen = True
        self.run = False

        # Alien
        self.alien_controller = AlienController(375, 375, 50, 50)
        self.alien_view = AlienView()
        self.alien_view.rect.topleft = self.alien_controller.rect.topleft

        # Pit
        self.pit = Pit(300, 0, 200, 10)

        # Start button
        start_img = pygame.transform.scale_by(
            pygame.image.load("start_button.png").convert_alpha(), 0.1
        )
        self.start_button = Button(300, 200, start_img)

        # Start background image
        background_img = pygame.image.load("start_screen.png").convert_alpha()
        self.start_screen_view = StartScreenView(background_img)

    def main_loop(self):
        """
        Runs the main game loop.
        """
        # Start screen
        while self.start_screen:
            # To close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            clicked = self.start_screen_view.draw(
                self.screen,
                self.alien_view,
                self.start_button,
            )

            if clicked:
                self.start_screen = False
                self.run = True

        # Update display
        pygame.display.update()
        # Frame Rate
        self.clock.tick(60)

        # Game loop
        while self.run:
            # Event handler
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    self.run = False

            # Key press
            keys = pygame.key.get_pressed()
            self.alien_controller.press_keys(keys)

            # Update controller
            self.alien_controller.update()
            self.alien_controller.check_pitfall(self.pit)

            # Update view
            self.alien_view.rect.topleft = self.alien_controller.rect.topleft
            self.alien_view.animate(self.alien_controller)

            # Draw everything
            self.screen.fill((0, 0, 0))
            self.alien_view.draw(self.screen, self.pit)

            # Check for death
            if not self.alien_controller.alive:
                self.run = False

            pygame.display.update()

            # Set framerate
            self.clock.tick(60)
        pygame.quit()

    def update_level(self):
        """
        If we want to add more levels
        """


class Pit:
    def __init__(self, x_pos, y_pos, width, height):
        self.starting_xy_wh = (x_pos, y_pos, width, height)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self._y_speed = 0.5
        self._width_scaler = 0.2
        self._height_scaler = 0.1
        self._left_or_right = 0

    def update(self):
        # When pit leaves the screen reset position and dimensions
        if self.y_pos > 599:
            self.x_pos = self.starting_xy_wh[0]
            self.y_pos = self.starting_xy_wh[1]
            self.width = self.starting_xy_wh[2]
            self.height = self.starting_xy_wh[3]
            # Random direction the pit goes
            if random.randint(0, 100) < 50:
                self._left_or_right = -1
            else:
                self._left_or_right = 1
        else:
            self.y_pos += self._y_speed
            self.x_pos += self._left_or_right / 5
            self.width += self._width_scaler
            self.height += self._height_scaler


if __name__ == "__main__":
    game = Game()
    game.main_loop()
