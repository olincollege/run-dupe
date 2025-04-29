import pygame


class Alien_Controller(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Constructs the alien as a sprite.

        Args:
            x: An integer representing the x value of the character.
            y: An integer representing the y value of the character.
        """
        super().__init__()

        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

        self.alive = True
        self.jumping = False
        self.on_ground = True
        self.jump_strength = -15
        self.gravity = 1
        self.velocity_x = 0
        self.velocity_y = 0

    def press_keys(self, keys):
        """_summary_

        Args:
            keys: A dictionary with keys that are integers for each key on the keyboard
            and values a value of 1 if it is being pressed or 0 if it is not being pressed.
        """
        # No x movement
        self.velocity_x = 0
        # Detect if keys are pressed
        if keys[pygame.K_LEFT]:
            self.velocity_x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = 5

        # Detect jump and run that function
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):
        """
        Makes the alien jumping by changing it's y position.
        """
        self.velocity_y = self.jump_strength
        self.on_ground = False
        self.jumping = True

    def update(self, platforms):
        """
        Change location of character, detect if on ground, and run animation loop.
        """
        # Move on left/right
        self.rect.x += self.velocity_x

        # Move up/down
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Check for collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # If its also falling (positive y)
                if self.velocity_y > 0:
                    # Place alien on top of platform
                    self.rect.bottom = platform.rect.top
                    # Stop falling
                    self.velocity_y = 0
                    self.on_ground = True
                    self.jumping = False

        # Check if on ground
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.velocity_y = 0
            self.on_ground = True

        # Check if misses platform
        if self.rect.y > 500 and not self.on_ground:
            self.alive = False


class Tunnel_Controller:
    def __init__(self):
        pass

    def update(self):
        pass


class Start_Screen_Controller:
    def __init__(self, image):
        """_summary_

        Args:
            x: An integer representing the x coordinate of the button.
            x: An integer representing the y coordinate of the button.
            image: A string of the path to the image of the button.
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.clicked = False

    def button_click(self):
        """_summary_"""
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over button
        if self.rect.collidepoint(pos):
            # Check if button is pressed for the first time
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
        return False
