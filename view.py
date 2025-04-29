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
        self.jumping = False

    def animate(self, controller):
        """
        Updates alien's graphic to one of three images to display running, jumping, and death.
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

    def draw(self, screen):
        """
        Draws character on screen using image.

        Args:
            screen: A surface object representing the game window.
        """
        screen.blit(self.image, self.rect)


class Tunnel_View:
    def __init__(self):
        pass

    def draw(self, screen):
        pass


class Start_Screen_View:
    def __init__(self, background_img):
        self.background_img = background_img
        self.background_rect = self.background_img.get_rect()
        self.speed_x = 0.2
        self.speed_y = 0.2

    def draw(self, screen, alien_view, button):
        """_summary_

        Args:
            surface: An image of the background to draw the button on.

        Returns:
            True if the button has been clicked, else returns False.
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
        alien_view.draw(screen)
        clicked = button.draw_button(screen)
        if clicked:
            return True
        pygame.display.update()
        return False
