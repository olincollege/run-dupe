"""_summary_

Returns:
    _type_: _description_
"""

import pygame


# Button class
class Button:
    """
    Represents a clickable button with a hover effect.

    Attributes:
        image: A string representing the path to the image representing the button.
            hover_image: A modified version of the orignal image.
        rect: An rectangle representing the button.
        clicked: A boolean representing whether or not the button has been clicked.
    """

    def __init__(self, x_pos, y_pos, image):
        """_summary_

        Args:
            x_val: An integer representing the x coordinate of the button.
            y_val: An integer representing the y coordinate of the button.
            image: A string of the path to the image of the button.
        """
        self.image = image
        self.hover_image = self._hover_button(image)
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))
        self.clicked = False

    def _hover_button(self, image, factor=1.3):
        # Creates a copy of the original image
        hover_image = image.copy()

        # Changes colors of image
        overlay = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        overlay.fill((50, 50, 50, 100))
        hover_image.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

        return hover_image

    def draw_button(self, screen):
        """_summary_

        Args:
            screen: An image of the background to draw the button on.

        Returns:
            A boolean of True if the button has been clicked, else returns False.
        """

        # Get mouse position
        pos = pygame.mouse.get_pos()

        current_image = self.hover_image if self.rect.collidepoint(pos) else self.image
        screen.blit(current_image, self.rect)

        # Handle click
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                return True

        # Reset button no not being pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return False

    def is_hovered(self):
        """Returns True if the mouse is hovering over the button."""
        return self.rect.collidepoint(pygame.mouse.get_pos())
