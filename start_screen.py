"""_summary_

Returns:
    _type_: _description_
"""

import pygame


# Button class
class Button:
    """_summary_"""

    def __init__(self, x, y, image):
        """_summary_

        Args:
            x: An integer representing the x coordinate of the button.
            x: An integer representing the y coordinate of the button.
            image: A string of the path to the image of the button.
        """
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw_button(self, screen):
        """_summary_

        Args:
            surface: An image of the background to draw the button on.

        Returns:
            True if the button has been clicked, else returns False.
        """
        screen.blit(self.image, self.rect)

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over button
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                return True

        # Reset button no not being pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return False
