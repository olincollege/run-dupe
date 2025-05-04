"""Contains the view classes for the game and the start screen."""

import pygame


class GameView(pygame.sprite.Sprite):
    """
    Draws the alien at the location of the controller.

    Args:
        pygame.sprite.Sprite: A class representing the characteristics
        of a sprite.

    Attributes:
        images: A dictionary with keys that are strings representing the
        titles of the
        images and values of surface objects of images for the character.
        image: A surface object of the current image the character is
        displaying.
        rect: A surface object representing the character.
        animation_timer: An integer representing the time in the character
        animation.
        jumping: A boolean representing if the character is jumping or not.
    """

    def __init__(self):
        """Initialize variables."""

        pygame.init()
        self.images = {
            "both": pygame.transform.scale_by(
                pygame.image.load("images/BOTH_legs.png").convert_alpha(), 0.5
            ),
            "left": pygame.transform.scale_by(
                pygame.image.load("images/LEFT_leg.png").convert_alpha(), 0.5
            ),
            "right": pygame.transform.scale_by(
                pygame.image.load("images/RIGHT_leg.png").convert_alpha(), 0.5
            ),
        }
        self.image = self.images["both"]
        self.rect = self.image.get_rect()
        self.animation_timer = 0
        self.jumping = False

    def animate(self, controller):
        """
        Updates the alien's graphic to one of three images to display
        running, jumping, and death.

        Args:
            controller: A class that acts as the controller for the alien.
        """
        # Define when the at rest image should be used
        if not controller.alive:
            self.image = self.images["both"]
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
            controller: A class that acts as the controller.
        """

        # Draw pit
        # Pits are slightly off color from the background for detection
        pygame.draw.rect(
            screen,
            pygame.Color(1, 1, 1),
            pygame.Rect(pit.x_pos, pit.y_pos, pit.width, pit.height),
        )

        # Pits stop appearing after character death
        if controller.alive:
            pit.update()

        # Draw Alien
        screen.blit(self.image, self.rect)

    def draw_level(self, screen, level):
        """
        Displays current level on screen.

        Args:
            screen: A surface object representing the game window.
            level: An integer representing the current level.
        """

        pygame.init()
        level_text = f"Level: {level}"
        font = pygame.font.SysFont("Arial", 30)
        text_surface = font.render(level_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))


class StartScreenView:
    """
    Draws the start screen and button.

    Attributes:
        background_img: An image object for the background of the start screen.
        background_rect: A rectangle object to display the background image on.
    """

    def __init__(self):
        """_
        Initializes the variables for the start screen.

        Args:
            background_img: A string representing the path to the image
            for the background.
        """
        self.background_img = pygame.transform.scale_by(
            pygame.image.load("images/start_screen.png").convert_alpha(), 0.6
        )
        self.background_rect = self.background_img.get_rect()
        self.alien_img = pygame.transform.scale_by(
            pygame.image.load("images/BOTH_legs.png").convert_alpha(), 0.8
        )
        self.alien_rect = self.alien_img.get_rect()
        self.alien_rect.center = (400, 400)
        self.background_rect.center = (400, 300)

    def draw(self, screen, button):
        """
        Draws the background and the button.

        Args:
            screen: A surface object representing the game window.
            button: The class that acts as the controller for the start button.

        Returns:
            A boolean of True if the button has been clicked, else
            returns False.
        """

        # Draw everything
        screen.fill((0, 0, 0))
        screen.blit(self.background_img, self.background_rect)
        screen.blit(self.alien_img, self.alien_rect)
        clicked = button.draw_button(screen)
        pygame.display.update()

        # Return when the button is clicked
        return clicked

    def pylint(self):
        """I have pylint."""
