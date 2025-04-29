"""
Add docstring
"""

import pygame
import start_screen
import alien
import tunnel


class Game:
    """
    Add docstring
    """

    def __init__(self):
        """
        Add docstring
        """
        pygame.init()

        # Make mouse visible
        pygame.mouse.set_visible(True)

        # Create display window
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Game objects
        self.alien = alien.Alien(100, 100)
        self.tunnel = tunnel.Tunnel()

        # Screen control
        self.start_screen = True
        self.run = False

        # Start button
        start_img = pygame.transform.scale_by(
            pygame.image.load("start_button.png").convert_alpha(), 0.1
        )
        self.start_button = start_screen.Button(300, 300, start_img)

        # Start background image
        self.background_img = pygame.image.load("start_screen.png").convert_alpha()
        self.background_rect = self.background_img.get_rect()
        self.speed_x = 1
        self.speed_y = 1

    def main_loop(self):
        # Start screen
        while self.start_screen:
            clicked, self.speed_x, self.speed_y = start_screen.draw_start(
                self.screen,
                self.alien,
                self.start_button,
                self.background_img,
                self.background_rect,
                self.speed_x,
                self.speed_y,
            )

            if clicked:
                self.start_screen = False
                self.run = True

        # Game loop
        while self.run:
            # Event handler
            for event in pygame.event.get():
                # Key press
                if event.type == pygame.KEYDOWN:
                    self.alien.press_keys(pygame.key.get_pressed())
                # Quit game
                if event.type == pygame.QUIT:
                    self.run = False

            # Update platforms for alien
            self.tunnel.update()
            self.alien.update(self.tunnel)

            # Draw everything
            self.screen.fill((0, 0, 0))
            self.tunnel.draw(self.screen)
            self.alien.draw(self.screen)

            pygame.display.update()

            # Set framerate
            self.clock.tick(60)
        pygame.quit()

    def update_level(self):
        """
        Add docstring
        """
        pass
