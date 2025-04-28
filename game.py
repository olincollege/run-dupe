"""
Add docstring
"""

import pygame
import start_screen
from alien import Alien
import tunnel


class Game:
    """
    Add docstring
    """

    def __init__(self):
        """
        Add docstring
        """
        # Make mouse visible
        pygame.mouse.set_visible(True)

        # Create display window
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.platforms = []
        self.alien = Alien
        self.platforms = []
        self.start_screen = True
        self.run = False

    def main_loop(self):
        pygame.init()
        pygame.display.init()
        # Load and resize start button image
        start_img = pygame.transform.scale_by(
            pygame.image.load("start_button.png").convert_alpha(), 0.1
        )
        start_button = start_screen.Button(300, 300, start_img)

        while self.start_screen:
            self.screen.fill((0, 0, 0))
            # Create start screen
            start_screen.draw_start(self.screen, self.alien)
            if not start_screen.Button.draw(self, self.screen):
                self.start_screen = False
                self.run = True

        while self.run:
            # Event handler
            for event in pygame.event.get():
                # Key press
                if event.type == pygame.KEYDOWN:
                    Alien.press_keys(self, pygame.key.get_pressed())
                # Quit game
                if event.type == pygame.QUIT:
                    self.run = False

            # Update platforms for alien
            Alien.update(self, self.platforms)

            # Draw everything
            self.screen.fill(0, 0, 0)
            pygame.Rect(self.screen)

            pygame.display.update()

            # Set framerate
            self.clock.tick(60)
        pygame.quit

    def update_level(self):
        """
        Add docstring
        """
        pass


Game.main_loop()
