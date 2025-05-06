"""Contains the controller classes for the character and the pits."""

import random
import pygame


class AlienController(pygame.sprite.Sprite):
    """
    Controls the player.

    Args:
        pygame.sprite.Sprite: A class representing the characteristics
        of a sprite.


    Attributes:
        width and height: Floats representing the width and height of
        the character.
        rect: A surface object representing the character.
        state: A dictionary with keys that are strings representing states
        that the character can be in (jumping and on the ground) and values
        of booleans representing if the states are true or false.
        alive: A boolean representing whether the character is alive.
        velocity_x and velocity_y: Floats representing the characters
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

        # Detect if keys are pressed and changes velocity
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.alive:
            self.velocity_x = -5
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.alive:
            self.velocity_x = 5

        # Detect jump and run that function
        if (
            (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w])
            and self.state["on_ground"]
            and self.alive
        ):
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

        # Checks for the color of the pit
        # Can only die when touching pit and on ground
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
        gravity = 0.75
        self.velocity_y += gravity
        self.rect.y += self.velocity_y
        self.state["jumping"] = True

        # Check if character has fallen off path or below the screen
        if (
            self.rect.top > 600
            or int(self.rect.left + self.width / 2) < 30
            or int(self.rect.right - self.width / 2) > 675
        ) and self.state["on_ground"] is True:
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
        starting_xy_wh: A list of floats representing the starting conditions
        of the pit.
        x_pos, y_pos: Floats representing the x and y positions of the pit.
        width, height: Floats representing the width and height of the pit.
        __y_speed: A float representing the speed that the pit approaches
        the character.
        _width_scalar, _height_scalar: A float representing the rate that the
        width and height of the pit is growing as it approaches the character.
        direction: A string randomly selected from a list to decide if the pit
        should go towards the left, right or center.
        pit_num: An integer representing the number of pits that have
        been created.
    """

    def __init__(self, x_pos, y_pos, width, height, speed, level):
        # pylint: disable=too-many-arguments

        """
        Initializes the variables to create the pit.

        Args:
            x_pos: A float representing the x position of the pit.
            y_pos: A float representing the y position of the pit.
            width: A float representing the width of the pit.
            height: A float representing the height of the pit.
            level: An integer representing the current level.
        """
        self.starting_xy_wh = (x_pos, y_pos, width, height)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height * level
        self._y_speed = speed
        self.pit_num = 0
        self._width_scaler = 2
        self._height_scaler = 1.4
        self.direction = 0

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

            # Random direction the pit goes and width
            self.direction = random.choice(["left", "center", "right"])
            if self.direction == "left":
                self.x_pos = 200
                self.width = random.choice([200, 300, 400])
            elif self.direction == "center":
                self.width = random.choice([200, 300, 400, 650])
            else:
                self.x_pos = 350
                self.width = random.choice([200, 300, 400])
        # Update pit position to move down the screen in direction
        else:
            self.y_pos += self._y_speed
            if self.direction == "left":
                self.x_pos -= 2.5
            elif self.direction == "right":
                self.x_pos += 1.5
            else:
                self.x_pos += 0
            self.width += self._width_scaler
            self.height += self._height_scaler

    def update_level(self, new_speed):
        """
        Changes speed for new level.

        Args:
            new_speed: An integer representing the updates speed.
        """
        self._y_speed = new_speed


class StartScreenController:
    """
    Represents a clickable button with a hover effect.

    Attributes:
        image: A Pygame surface object showing the button's image.
        hover_image: A modified version of the original image.
        rect: An rectangle representing the button.
        clicked: A boolean representing whether or not the button has
        been clicked.
    """

    def __init__(self, x_pos, y_pos):
        """
        Initialize attributes for start screen controller.

        Args:
            x_pos: An integer representing the x coordinate of the button.
            y_pos: An integer representing the y coordinate of the button.
        """
        pygame.init()
        self.image = pygame.transform.scale_by(
            pygame.image.load("images/start_button.png").convert_alpha(), 0.1
        )
        self.hover_image = self._hover_button(self.image)
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))
        self.clicked = False

    def _hover_button(self, image):
        """
        Recolors an image.

        Args:
            image: A Pygame surface object representing the button's image.

        Returns:
             A Pygame surface object showing button's image that has been recolored.
        """
        # Creates a copy of the original image
        hover_image = image.copy()

        # Changes colors of image
        overlay = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        overlay.fill((50, 50, 50, 100))
        hover_image.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

        return hover_image

    def draw_button(self, screen):
        """
        Draws the button and checks if it has been clicked.

        Args:
            screen: A Pygame surface object showing an image of the background to draw the button on.

        Returns:
            A boolean of True if the button has been clicked, else
            returns False.
        """

        # Get mouse position
        pos = pygame.mouse.get_pos()

        current_image = (
            self.hover_image if self.rect.collidepoint(pos) else self.image
        )
        screen.blit(current_image, self.rect)

        # When button is clicked
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                return True

        # Reset button to not being pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return False

    def is_hovered(self):
        """Returns True if the mouse is hovering over the button."""
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def reset(self):
        """Resets the button to not being clicked."""
        self.clicked = False
