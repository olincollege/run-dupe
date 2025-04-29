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

    def draw_button(self, surface):
        """_summary_

        Args:
            surface (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over button
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True

        # Reset button no not being pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return self.clicked


def draw_start(
    screen, alien, button, background_img, background_rect, speed_x, speed_y
):

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
    screen.fill(0, 0, 0)
    screen.blit(background_img, background_rect)

    # Draw alien
    alien.draw(screen)

    # Draw button
    clicked = button.draw_button(screen)

    pygame.display.update

    return clicked, speed_x, speed_y
