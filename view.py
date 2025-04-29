import pygame


class Alien_View(pygame.sprite.Sprite):
    def __init__(self):
        self.images = {
            "both": pygame.image.load("character_images/both_legs.png"),
            "left": pygame.image.load("character_images/left_leg.png"),
            "right": pygame.image.load("character_images/right_leg.png"),
        }
        self.image = self.images["both"]
        self.rect = self.image.get_rect()
        self.animation_timer = 0

    def animate(self):
        """
        Updates alien's graphic to one of three images to display running, jumping, and death.
        """
        # Define when the at rest image should be used
        if not self.alive:
            self.image = self.images["both"]
        elif self.jumping:
            self.image = self.images["both"]
        # Otherwise switch between left and right leg forward every 200 ms
        else:
            current_time = pygame.time.get_ticks()
            if current_time - self.animation_timer > 200:
                if self.image == self.images["left"]:
                    self.image = self.images["right"]
                else:
                    self.image = self.images["left"]
            self.animation_timer = current_time
        self.animation_timer = 0

    def draw(self, screen):
        """
        Draws character on screen using image.

        Args:
            screen: A surface object representing the game window.
        """
        screen.blit(self.image, self.rect)


class Tunnel_View:
    pass


class Start_Screen_View:
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
            surface: An image of the background to draw the button on.

        Returns:
            True if the button has been clicked, else returns False.
        """

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return self.clicked


def draw_start(
    screen, alien, button, background_img, background_rect, speed_x, speed_y
):
    """_summary_

    Args:
        screen: A surface object representing the game window.
        alien (_type_): _description_
        button (_type_): _description_
        background_img: An image to be displayed in the background.
        background_rect (_type_): _description_
        speed_x: An integer representing the speed in the x direction.
        speed_y: An integer representing the speed in the y direction.

    Returns:
        _type_: _description_
    """

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
    screen.fill((0, 0, 0))
    screen.blit(background_img, background_rect)

    # Draw alien
    alien.draw(screen)

    # Draw button
    clicked = button.draw_button(screen)

    pygame.display.update

    return clicked, speed_x, speed_y
