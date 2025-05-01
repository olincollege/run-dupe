"""_summary_

Returns:
    _type_: _description_
"""

import pygame


# pylint: disable=too-few-public-methods
class AlienController(pygame.sprite.Sprite):
    """_summary_

    Args:
        pygame (_type_): _description_
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

        self.alive = True
        self.jumping = False
        self.on_ground = True
        self.jump_strength = -20
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
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):
        """
        Makes sets up the alien to jump.
        """
        self.velocity_y = self.jump_strength
        self.on_ground = False
        self.jumping = True

    def check_pitfall(self, pit):
        """
        Checks if the character has fallen into the pit.

        Args:
            pit: A class representing the creation and location of the pits.

        Returns:
            A boolean, True if the character is alive and has not fallen into the
            pit and False if the character is dead and has fallen into the pit.
        """
        if (
            pit.y_pos == 400
            and pit.x_pos < self.rect.x + 10
            and pit.x_pos + 200 > self.rect.x + 10
            and not self.jumping
        ):
            self.alive = False
        return self.alive

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
        self.jumping = False

        if (
            self.rect.top > 600
            or int(self.rect.left + self.width / 2) < 0
            or int(self.rect.right - self.width / 2) > 800
        ):
            self.alive = False

        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.on_ground = True


# class StartScreenController:
#     """
#     Sets up the start screen with the start button.
#     """

#     def __init__(self, image):
#         """
#         Sets up image in pygame format.

#         Args:
#             image: A string of the path to the image of the button.
#         """
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.clicked = False

#     def button_click(self):
#         """
#         Detects and handles if the button has been clicked.

#         Returns:
#             A boolean of True if the button has been clicked, else returns False.
#         """

#         # Get mouse position
#         pos = pygame.mouse.get_pos()

#         # Check mouse over button
#         if self.rect.collidepoint(pos):
#             # Check if button is pressed for the first time
#             if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
#                 self.clicked = True
#         return False
