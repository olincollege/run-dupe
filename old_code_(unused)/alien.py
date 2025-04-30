"""
Add docstring
"""

import pygame


class Alien(pygame.sprite.Sprite):
    """
    Add docstring

    Attributes:
        images: A dictionary with keys that are strings for the image titles and
        values that load the strings of paths to the images.
        image: An image to be displayed.
        rect: An object representing the character.
        x: An integer representing the characters current x position.
        y: An integer representing the characters current y position.
        alive: A boolean representing whether the character is currently alive.
        jumping: A boolean representing whether the character is currently jumping.
        on_ground: A boolean representing whether the character is currently on the ground.
        jump_strength: An integer representing the strength of the character's jump.
        gravity: An integer representing the strength of gravity.
        velocity_x: An integer representing the characters current x velocity.
        velocity_y: An integer representing the characters current y velocity.
        animation_timer: An integer representing the current time for the animation.
    """

    def __init__(self, x, y):
        """
        Constructs the alien as a sprite.

        Args:
            x: An integer representing the x value of the character.
            y: An integer representing the y value of the character.
        """
        super().__init__()
        self.images = {
            "both": pygame.image.load("character_images/both_legs.png"),
            "left": pygame.image.load("character_images/left_leg.png"),
            "right": pygame.image.load("character_images/right_leg.png"),
        }
        self.image = self.images["both"]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

        self.alive = True
        self.jumping = False
        self.on_ground = True
        self.jump_strength = -15
        self.gravity = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.animation_timer = 0

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

        self.animate()

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
