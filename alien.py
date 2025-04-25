"""
Add docstring
"""

import time
import pygame


# 	class alien (just the player)
# 		init
# 			alien_state (dead or alive, running or stopped)
# 		def update_alien
# 			while not dead
# 			animate legs moving: every second it switched between two images, pause when jumping
# 			alien stays upright at all times
# 			Animate legs for jump
# 			else
# 			stop moving
# 		def jump
# 			alien_go_up: when space bar is clicked, alien goes up first and then down (original pos) along the y-axis
#       def x_change
#           while running:
#             when < is pressed change x by negative something
#             when > is pressed change x by positive something


class Alien(pygame.sprite.Sprite):
    """
    Add docstring
    """

    def __init__(self, x, y):
        """
        Constructs the alien as a sprite.

        Args:
            x: An integer representing the x value of the character.
            y: An integer representing the y value of the character.

        Attributes:

        """
        self.image = pygame.image.load("character_images/both_legs.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.color = (0, 128, 255)
        self.alive = True
        self.velocity_y = 0
        self.jump_strength = -15
        self.gravity = 1
        self.original_y = y
        self.on_ground = True
        self.jumping = False

    def x_change(self):
        run = True
        velocity_x = 10
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT[]:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= velocity_x
            if keys[pygame.K_RIGHT]:
                self.x += velocity_x

    def alien_go_down(self):
        """
        Updates the position of the alien to return down to the ground after jumping
        """
        if not self.on_ground:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            # Go back down to original y value
            if self.rect.y >= self.original_y:
                self.rect.y = self.original_y
                self.velocity_y = 0
                self.on_ground = True
                self.jumping = False

    def jump(self):
        """
        Makes the alien jumping by changing it's y position.
        """
        if self.on_ground and self.alive:
            self.velocity_y = self.jump_strength
            self.on_ground = False
            self.jumping = True

    def alien_death(self):
        """
        Updates the alien's status from alive to dead when it falls.
        """
        # How to detect death
        black = [0, 0, 0]
        if pygame.Surface.get_at(self.x, self.y) == black and self.on_ground:
            self.alive = False

    def animate_alien(self):
        """
        Updates alien's graphic to one of three images to display running, jumping, and death.
        """
        while self.alive and not self.jumping:
            self.image = pygame.image.load("character_images/left_leg.png")
            time.sleep(0.5)
            self.image = pygame.image.load("character_images/right_leg.png")
            time.sleep(0.5)
            self.image = pygame.image.load("character_images/both_legs.png")
        else:
            self.image = pygame.image.load("character_images/both_legs.png")
