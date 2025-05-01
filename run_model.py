"""_summary_"""

import random
import pygame
from run_view import AlienView, StartScreenView
from run_controller import AlienController
from run_start_screen import Button


class Game:
    """
    Runs the main game loop.

    Attributes:
        screen and clock: Pygame classes that set up the game.
        start_screen and run: Booleans that represent the state of the game.
        alien_controller and alien_view: Classes that represent the controller
        and view the game.
        level and pit_speed: Integers that represent the level and the
        speed that the pits approach the character.
        pit: A class that creates the pits.
        start_button and start_screen_view: Classes that represent the start button
        and the view of the start screen.
    """

    def __init__(self):
        pygame.init()

        # Make mouse visible
        pygame.mouse.set_visible(True)

        # Create display window
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Which screen is showing
        self.start_screen = True
        self.run = False

        # Alien
        self.alien_controller = AlienController(375, 375, 50, 50)
        self.alien_view = AlienView()
        self.alien_view.rect.topleft = self.alien_controller.rect.topleft

        # Pit
        self.level = 0
        self.pit_speed = 3.5
        self.pit = Pit(300, 0, 200, 10, self.pit_speed, self.level)
        self.update_level()

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
            self.alien_controller.check_pitfall(self.screen)

            # Update view
            self.alien_view.rect.topleft = self.alien_controller.rect.topleft
            self.alien_view.animate(self.alien_controller)

            # Draw everything
            self.screen.fill((0, 0, 0))
            self.alien_view.draw(self.screen, self.pit)

            # Check for death
            if not self.alien_controller.alive:
                pass

            # Next level
            if self.pit.pit_num == 5:
                self.pit.pit_num = 0
                self.update_level()

            pygame.display.update()

            # Set framerate
            self.clock.tick(60)
        pygame.quit()

    def update_level(self):
        """
        Changes speed that platforms approach at each level.
        """

        self.level += 1
        print(self.level)
        print("new level")
        self.pit_speed += 3
        print(self.pit_speed)


class Pit:
    """
    Creates a pit.

    Attributes:
        x_pos, y_pos: Integers representing the x and y positions of the pit.
        width, height: Integers representing the width and height of the pit.
        __y_speed: A float representing the speed that the pit approaches the character.
        _width_scalar, _height_scalar: A float representing the rate that the width and
        height of the pit is growing as it approaches the character.
        _left_or_right: An integer representing which direction the pit should approach
        the character from, -1 for left and 1 for right.
        pit_num: An integer representing the number of pits that have been created.
    """

    def __init__(self, x_pos, y_pos, width, height, speed, level):
        """
        Initializes the variables to create the pit.

        Args:
            x_pos: An integer representing the x position of the pit.
            y_pos: An integer representing the y position of the pit.
            width: An integer representing the width of the pit.
            height: An integer representing the height of the pit.
            level: An integer representing the current level.
        """
        self.starting_xy_wh = (x_pos, y_pos, width, height)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height * level
        self._y_speed = speed
        self._width_scaler = 0.2
        self._height_scaler = 0.4
        self._left_or_right = 0
        self.pit_num = 0

    def update(self):
        """
        Updates the position and dimensions of the pit as it approaches the character.
        """
        # When pit leaves the screen reset position and dimensions
        if self.y_pos > 599:
            self.pit_num += 1
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
