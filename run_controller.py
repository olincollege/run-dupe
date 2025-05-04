"""Contains the controller classes for the character and the pits."""

import random
import pygame


class AlienController(pygame.sprite.Sprite):
    """_summary_

    Args:
        pygame.sprite.Sprite: A class representing the characteristics
        of a sprite.


    Attributes:
        width and height: Integers representing the width and height of
        the character.
        rect: A surface object representing the character.
        state: A dictionary with keys that are strings representing states
        that the character can be in and values of booleans.
        alive: A boolean representing whether the character is alive.
        velocity_x and velocity_y: Integers representing the characters
        x and y velocities.
    """

    def __init__(self, x_pos, y_pos, width, height):
        """
        Constructs the alien as a sprite.

        Args:
            x_pos: An integer representing the x value of the character.
            y_pos: An integer representing the y value of the character.
            width: An integer representing the width of the character.
            height: An integer representing the height of the character.
        """
        super().__init__()

        self.width = width
        self.height = height
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.state = {"jumping": False, "on_ground": True}
        self.alive = True
        self.velocity_x = 0
        self.velocity_y = 0

    def press_keys(self, keys):
        """
        Collects data of which keys have been pressed.

        Args:
            keys: A dictionary with keys that are integers for each key on
            the keyboard and values a value of 1 if it is being pressed or
            0 if it is not being pressed.
        """
        # No x movement
        self.velocity_x = 0
        # Detect if keys are pressed
        if keys[pygame.K_LEFT] and self.alive:
            self.velocity_x = -5
        elif keys[pygame.K_RIGHT] and self.alive:
            self.velocity_x = 5

        # Detect jump and run that function
        if keys[pygame.K_SPACE] and self.state["on_ground"] and self.alive:
            self.jump()

    def jump(self):
        """
        Makes sets up the alien to jump.
        """
        self.velocity_y = -20
        self.state["on_ground"] = False
        self.state["jumping"] = True

    def check_pitfall(self, surface):
        """
        Checks if the character has fallen into the pit.

        Args:
            surface: A surface object representing the game window.

        Returns:
            A boolean, True if the character is alive and has not fallen
            into the pit and False if the character is dead and has fallen
            into the pit.
        """

        if self.state["on_ground"] and surface.get_at(
            ((self.rect.x), self.rect.bottom + 100)
        ) == (
            1,
            1,
            1,
        ):
            self.alive = False

    def update(self):
        """
        Update the character to change location when keys are pressed,
        detect if its on ground, and detect if it dies.
        """
        # Move on left/right
        self.rect.x += self.velocity_x

        # Move up/down
        gravity = 0.5
        self.velocity_y += gravity
        self.rect.y += self.velocity_y
        self.state["jumping"] = True

        # Check if walked off screen
        if (
            self.rect.top > 600
            or int(self.rect.left + self.width / 2) < 30
            or int(self.rect.right - self.width / 2) > 675
        ):
            self.alive = False

        # Keep feet on ground
        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.state["on_ground"] = True
            self.state["jumping"] = False


class PitController:
    # pylint: disable=too-many-instance-attributes
    """
    Creates a pit.

    Attributes:
        starting_xy_wh: A list of integers representing the starting conditions
        of the pit.
        x_pos, y_pos: Integers representing the x and y positions of the pit.
        width, height: Integers representing the width and height of the pit.
        __y_speed: A float representing the speed that the pit approaches
        the character.
        _width_scalar, _height_scalar: A float representing the rate that the
        width and height of the pit is growing as it approaches the character.
        _left_or_right: An integer representing which direction the pit
        should approach the character from, -1 for left and 1 for right.
        pit_num: An integer representing the number of pits that have
        been created.
    """

    def __init__(self, x_pos, y_pos, width, height, speed, level):
        # pylint: disable=too-many-arguments

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
        self.pit_num = 0
        self._width_scaler = 0.2
        self._height_scaler = 0.4
        self._left_or_right = 0

    def update(self):
        """
        Updates the position and dimensions of the pit as it approaches
        the character.
        """
        # When pit leaves the screen reset position and dimensions
        if self.y_pos > 599:
            self.pit_num += 1
            self.x_pos = self.starting_xy_wh[0]
            self.y_pos = self.starting_xy_wh[1]
            self.width = self.starting_xy_wh[2]
            self.height = self.starting_xy_wh[3]
            # Random direction the pit goes
            direction = random.randint(0, 3)
            if direction == 0:
                self._left_or_right = -1
            elif direction == 1:
                self._left_or_right = 0
            else:
                self._left_or_right = 1
        else:
            self.y_pos += self._y_speed
            self.x_pos += self._left_or_right / 5 + self._left_or_right * 2
            self.width += self._width_scaler
            self.height += self._height_scaler
        print(self._y_speed)

    def update_level(self, new_speed):
        self._y_speed = new_speed

    def i_hate_pylint(self):
        """Self explanatory"""
