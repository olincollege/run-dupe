"""_summary_

Returns:
    _type_: _description_
"""

import pygame


class AlienView(pygame.sprite.Sprite):
    """
    Draws the alien at the location of the controller.

    Args:
        pygame.sprite.Sprite: A class representing the characteristics of a sprite.

    Attributes:
        images: A dictionary with keys that are strings representing the titles of the
        images and values of surface objects of images for the character.
        image: A surface object of the current image the character is displaying.
        rect: A surface object representing the character.
        animation_timer: An integer representing the time in the character animation.
        jumping: A boolean representing if the character is jumping or not.
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
            controller: A class that acts as the controller for the alien.
        """
        # Define when the at rest image should be used
        if not controller.alive:
            self.image = self.images["both"]
            for i in range(5):
                pygame.transform.rotate(self.image, i * 90)
        elif controller.state["jumping"]:
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

    def draw(self, screen, pit, controller):
        """
        Draws character on screen using image.

        Args:
            screen: A surface object representing the game window.
            pit: A class that creates the pit.
        """

        # Draw pit
        pygame.draw.rect(
            screen,
            pygame.Color(50, 50, 50),
            pygame.Rect(pit.x_pos, pit.y_pos, pit.width, pit.height),
        )
        if controller.alive:
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
        self.background_img = pygame.transform.scale_by(background_img, 0.6)
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (400, 300)

    def draw(self, screen, button):
        """_summary_

        Args:
            screen: A surface object representing the game window.
            button: The class that acts as the view for the start button.

        Returns:
            A boolean of True if the button has been clicked, else returns False.
        """

        # Draw everything
        screen.fill((0, 0, 0))
        screen.blit(self.background_img, self.background_rect)
        clicked = button.draw_button(screen)
        pygame.display.update()
        return clicked

    def pylint(self):
        """Satisfy pylint"""
