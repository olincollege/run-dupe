import pygame
from view import Alien_View, Tunnel_View, Start_Screen_View
from controller import (
    Alien_Controller,
    Tunnel_Controller,
    Start_Screen_Controller,
    Platform,
)
from start_screen import Button

"""
Add docstring
"""


class Game:
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
        self.alien_controller = Alien_Controller(375, 375)
        self.alien_view = Alien_View()
        self.alien_view.rect.topleft = self.alien_controller.rect.topleft

        # Tunnel
        self.tunnel_controller = Tunnel_Controller()
        self.tunnel_view = Tunnel_View()

        # Start button
        start_img = pygame.transform.scale_by(
            pygame.image.load("start_button.png").convert_alpha(), 0.1
        )
        self.start_button = Button(300, 200, start_img)

        # Start background image
        background_img = pygame.image.load("start_screen.png").convert_alpha()
        self.start_screen_view = Start_Screen_View(background_img)

    def main_loop(self):
        # Start screen
        while self.start_screen:
            # To close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            clicked = self.start_screen_view.draw(
                self.screen, self.alien_view, self.start_button
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
            platforms = self.tunnel_controller.update()
            self.alien_controller.update(platforms)

            # Update view
            self.alien_view.rect.topleft = self.alien_controller.rect.topleft
            self.alien_view.animate(self.alien_controller)

            # Draw everything
            self.screen.fill((0, 0, 0))
            self.tunnel_view.draw(platforms, self.screen)
            self.alien_view.draw(self.screen)

            pygame.display.update()

            # Set framerate
            self.clock.tick(60)
        pygame.quit()

    def update_level(self):
        """
        Add docstring
        """
        pass


if __name__ == "__main__":
    game = Game()
    game.main_loop()
