"""Runs the game."""

import pygame
from run_view import GameView, StartScreenView
from run_controller import AlienController, PitController
from run_start_screen import Button


class Game:
    """
    Runs the main game loop.

    Attributes:
        screen and clock: Pygame classes that set up the game.
        start_screen and run: Booleans that represent the state of the game.
        alien_controller and game_view: Classes that represent the controller
        and view the game.
        start_button and start_screen_view: Classes that represent the
        start button and the view of the start screen.
        properties: A dictionary with keys of strings representing game
        properties and values of floats that represent the level and the
        speed that the pits approach the character.
        which_screen: A dictionary with keys of string representing the
        two displays and values of booleans with True if that display is
        being shown, else False.
    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        pygame.init()

        # Make mouse visible
        pygame.mouse.set_visible(True)

        # Create display window
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Load classes for game controller and view
        self.alien_controller = AlienController(375, 375, 50, 50)
        self.game_view = GameView()
        self.game_view.rect.topleft = self.alien_controller.rect.topleft

        # Load image and class for start button
        start_img = pygame.transform.scale_by(
            pygame.image.load("images/start_button.png").convert_alpha(), 0.1
        )
        self.start_button = Button(300, 200, start_img)

        # Load image and class for start screen background
        background_img = pygame.image.load(
            "images/start_screen.png"
        ).convert_alpha()
        self.start_screen_view = StartScreenView(background_img)

        # Initialize some game properties
        self.properties = {"level": 1, "pit_speed": 3.5}
        self.which_screen = {"start_screen": True, "run": False}

    def main_loop(self):
        """
        Runs the main game loop.
        """

        # Game background image
        background = pygame.image.load("images/background.png").convert_alpha()

        while True:
            # Start screen display
            while self.which_screen["start_screen"]:
                # To close the game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                # Draw start screen and start button
                clicked = self.start_screen_view.draw(
                    self.screen,
                    self.start_button,
                )

                # If start button is clicked change displays to game running
                if clicked:
                    self.which_screen["start_screen"] = False
                    self.which_screen["run"] = True

            # Update display
            pygame.display.update()

            # Frame Rate
            self.clock.tick(60)

            # Create a pit
            pit = PitController(
                300,
                0,
                200,
                10,
                self.properties["pit_speed"],
                self.properties["level"],
            )

            # Game loop
            while self.which_screen["run"]:
                # Event handler
                for event in pygame.event.get():
                    # Quit game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                # Key press
                keys = pygame.key.get_pressed()
                self.alien_controller.press_keys(keys)

                # Update controller
                self.alien_controller.update()
                self.alien_controller.check_pitfall(self.screen)

                # Update view location and animation
                self.game_view.rect.topleft = self.alien_controller.rect.topleft
                self.game_view.animate(self.alien_controller)

                # Draw background display
                self.screen.fill((0, 0, 0))
                self.screen.blit(background, (0, 0))

                # Update pit location
                pit.update()

                # Draw character and pits
                self.game_view.draw(self.screen, pit, self.alien_controller)
                self.game_view.draw_level(self.screen, self.properties["level"])

                # If character dies reset game
                if not self.alien_controller.alive:
                    self.reset_game()
                    break

                # New level after passing 5 pits
                if pit.pit_num == 5:
                    self.update_level()
                    pit = PitController(
                        300,
                        0,
                        200,
                        10,
                        self.properties["pit_speed"],
                        self.properties["level"],
                    )

                # Update display
                pygame.display.update()

                # Set framerate
                self.clock.tick(60)

    def update_level(self):
        """
        Changes speed that platforms approach at each level and level number.
        """

        self.properties["level"] += 1
        # Speed up pit approaches for first 8 levels
        # (it gets too fast after that)
        if 1 <= self.properties["level"] < 8:
            self.properties["pit_speed"] += 1

    def reset_game(self):
        """
        Resets the game after death to original properties.
        """

        self.properties["level"] = 1
        self.properties["pit_speed"] = 3.5

        self.alien_controller.rect.topleft = (375, 375)
        self.alien_controller.velocity_x = 0
        self.alien_controller.velocity_y = 0
        self.alien_controller.state = {"jumping": False, "on_ground": True}
        self.alien_controller.alive = True

        self.game_view.rect.topleft = self.alien_controller.rect.topleft

        self.start_button.clicked = False
        self.which_screen = {"start_screen": True, "run": False}


if __name__ == "__main__":
    game = Game()
    game.main_loop()
