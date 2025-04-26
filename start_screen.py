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
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        """_summary_

        Args:
            surface (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Get mouse position
        start_game = False
        pos = pygame.mouse.get_pos()

        # Check mouse over button
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                start_game = True

        # Reset button no not being pressed
        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return start_game
