"""_summary_

Returns:
    _type_: _description_
"""

import pygame

# pylint: disable=too-few-public-methods


class AlienView(pygame.sprite.Sprite):
    """_summary_

    Args:
        pygame (_type_): _description_
    """

    def __init__(self):
        self.images = {
            "both": pygame.image.load("character_images/both_legs.png"),
            "left": pygame.image.load("character_images/left_leg.png"),
            "right": pygame.image.load("character_images/right_leg.png"),
        }
        self.image = self.images["both"]
        self.rect = self.image.get_rect()
        self.animation_timer = 0
        self.jumping = False

    def animate(self, controller):
        """
        Updates the alien's graphic to one of three images to display running, jumping, and death.

        Args:
            controller: The class that acts as the controller for the alien.
        """
        # Define when the at rest image should be used
        if not controller.alive:
            self.image = self.images["both"]
        elif controller.jumping:
            self.image = self.images["both"]
        # Otherwise switch between left and right leg forward every 200 ms
        else:
            current_time = pygame.time.get_ticks()
            if current_time - self.animation_timer > 200:
                self.image = (
                    self.images["right"]
                    if self.image == self.images["left"]
                    else self.images["left"]
                )
                self.animation_timer = current_time

    def draw(self, screen, pit):
        """
        Draws character on screen using image.

        Args:
            screen: A surface object representing the game window.
        """

        # Draw pit
        pygame.draw.rect(
            screen,
            pygame.Color(50, 50, 50),
            pygame.Rect(pit.x_pos, pit.y_pos, pit.width, pit.height),
        )
        pit.update()
        # Draw Alien
        screen.blit(self.image, self.rect)


class StartScreenView:
    """
    Draws the start screen and button.
    """

    def __init__(self, background_img):
        """_
        Initializes the variables for the start screen.

        Args:
            background_img: A string representing the path to the image for the background.
        """
        self.background_img = background_img
        self.background_rect = self.background_img.get_rect()
        self.speed_x = 0.2
        self.speed_y = 0.2

    def draw(self, screen, alien_view, button):
        """_summary_

        Args:
            screen: A surface object representing the game window.
            alien_view: The class that acts as the view for the alien.
            button: The class that acts as the view for the start button.

        Returns:
            A boolean of True if the button has been clicked, else returns False.
        """

        # Animate background
        self.background_rect.x += self.speed_x
        self.background_rect.y += self.speed_y

        # Change direction if image hits boundary
        if (
            self.background_rect.left <= 0
            or self.background_rect.right >= screen.get_width()
        ):
            self.speed_x *= -1
        if (
            self.background_rect.top <= 0
            or self.background_rect.bottom >= screen.get_height()
        ):
            self.speed_y *= -1

        # Draw everything
        screen.fill((0, 0, 0))
        screen.blit(self.background_img, self.background_rect)
        clicked = button.draw_button(screen)
        if clicked:
            return True
        pygame.display.update()
        return False
