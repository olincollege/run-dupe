"""_summary_

Returns:
    _type_: _description_
"""

import random
import pygame


# pylint: disable=too-few-public-methods
class AlienController(pygame.sprite.Sprite):
    """_summary_

    Args:
        pygame (_type_): _description_
    """

    def __init__(self, x_pos, y_pos):
        """
        Constructs the alien as a sprite.

        Args:
            x_pos: An integer representing the x value of the character.
            y_pos: An integer representing the y value of the character.
        """
        super().__init__()

        self.rect = pygame.Rect(x_pos, y_pos, 50, 50)

        self.alive = True
        self.jumping = False
        self.on_ground = True
        self.jump_strength = -15
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

    def update(self, platforms):
        """
        Update the character to change location when keys are pressed,
        detect if its on ground, and detect if it dies.

        Args:
            platforms: A list representing the positions of all the platforms.
        """
        # Move on left/right
        self.rect.x += self.velocity_x

        # Move up/down
        gravity = 1
        self.velocity_y += gravity
        self.rect.y += self.velocity_y

        # Check for collisions
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # If its also falling (positive y)
                if self.velocity_y > 0:
                    # Place alien on top of platform
                    self.rect.bottom = platform.rect.top
                    # Stop falling
                    self.velocity_y = 0
                    self.on_ground = True
                    self.jumping = False

        # Check if on ground
        if self.rect.top > 600:  # screen height
            self.alive = False

        # Check if misses platform
        if self.rect.y > 500 and not self.on_ground:
            self.alive = False


class Platform:
    """
    Creates one platform.
    """

    def __init__(self, x_pos, y_pos, width, height):
        """
        Constructs a platform.

        Args:
            x_pos: An integer representing the x location of the platform.
            y_pos: An integer representing the y location of the platform.
            width: An integer representing the width of the platform
            height: An integer representing the height of the platform
        """
        self.rect = pygame.Rect(x_pos, y_pos, width, height)


class TunnelController:
    """
    Creates the platforms for the level.
    """

    def __init__(self):
        self.platforms = []
        self.scroll_speed = 3
        self.platform_direction_rand = "right"
        self.generate_platforms()

    def generate_platforms(self):
        """
        Creates multiple platforms.
        """
        for i in range(5):
            x_pos = 200 + i * 150
            y_pos = 450
            width = 100
            height = 20
            self.platforms.append(Platform(x_pos, y_pos, width, height))

    def update(self):
        """_summary_

        Returns:
            A list of the positions of the platforms.
        """
        # Random if platform goes right or left
        self.platform_direction_rand = random.choice(["right", "left"])

        # Scroll platforms
        for platform in self.platforms:
            if self.platform_direction_rand == "right":
                platform.rect.x -= self.scroll_speed
            elif self.platform_direction_rand == "left":
                platform.rect.x += self.scroll_speed

        # Remove off screen platforms
        self.platforms = [p for p in self.platforms if p.rect.right > 0]

        return self.platforms


class StartScreenController:
    """
    Sets up the start screen with the start button.
    """

    def __init__(self, image):
        """
        Sets up image in pygame format.

        Args:
            image: A string of the path to the image of the button.
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.clicked = False

    def button_click(self):
        """
        Detects and handles if the button has been clicked.

        Returns:
            A boolean of True if the button has been clicked, else returns False.
        """

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over button
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
        return False
