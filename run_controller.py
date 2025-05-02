"""_summary_

Returns:
    _type_: _description_
"""

import pygame


class AlienController(pygame.sprite.Sprite):
    """_summary_

    Args:
        pygame.sprite.Sprite: A class representing the characteristics of a sprite.


    Attributes:
        width and height: Integers representing the width and height of the character.
        rect: A surface object representing the character.
        alive, jumping, and on_ground: Booleans representing whether the character is alive,
        jumping, or on the ground.
        velocity_x and velocity_y: Integers representing the characters x and y velocities.
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
            keys: A dictionary with keys that are integers for each key on the keyboard
            and values a value of 1 if it is being pressed or 0 if it is not being pressed.
        """
        # No x movement
        self.velocity_x = 0
        # Detect if keys are pressed
        if keys[pygame.K_LEFT]:
            self.velocity_x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = 5

        # Detect jump and run that function
        if keys[pygame.K_SPACE] and self.state["on_ground"]:
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
            A boolean, True if the character is alive and has not fallen into the
            pit and False if the character is dead and has fallen into the pit.
        """

        if self.state["on_ground"] and surface.get_at(
            ((self.rect.x), self.rect.bottom + 75)
        ) == (
            50,
            50,
            50,
        ):
            self.alive = False
            print("dead hehe")

    # Not using rn
    def check_next_level(self, surface):
        """
        Checks if the character should move onto the nextlevel.

        Args:
            surface: A surface object representing the game window.
        """
        if surface.get_at(self.rect) == (0, 0, 255):
            self.alive = False
            print("next level")

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

        if (
            self.rect.top > 600
            or int(self.rect.left + self.width / 2) < 0
            or int(self.rect.right - self.width / 2) > 800
        ):
            self.alive = False

        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.state["on_ground"] = True
            self.state["jumping"] = False
