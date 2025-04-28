"""_summary_

Returns:
    _type_: _description_
"""

import random
import pygame
import time


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
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return start_game


def draw_start(screen, alien):
    # Load background image
    background_img = pygame.image.load("start_screen.png").convert_alpha()
    background_rect = background_img.get_rect()

    # Set initial position for background image
    background_rect.x = random.randint(0, screen.get_width() - background_rect.width)
    background_rect.y = random.randint(0, screen.get_height() - background_rect.height)
    speed_x = 1
    speed_y = 1

    screen.fill(0, 0, 0)

    # Animate background
    background_rect.x += speed_x
    background_rect.y += speed_y

    # Change direction if image hits boundary
    if (
        background_rect.x <= 0
        or background_rect.x >= screen.get_width() - background_rect.width
    ):
        speed_x *= -1
    if (
        background_rect.y <= 0
        or background_rect.y >= screen.get_height() - background_rect.height
    ):
        speed_y *= -1

    # Draw background on screen
    screen.blit(background_img, background_rect)

    # Draw alien
    alien.draw(screen)

    # Draw start button and check if it's clicked
    if start_button.draw(screen):
        return True

    pygame.display.update
    pygame.time.Clock().tick(60)
