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


class Alien(pygame.sprite.Sprite):
    """
    Add docstring
    """

    def __init__(self, x, y):
        """
        Constructs the alien as a sprite.

        Attributes:
            color: A list representing the color of the alien.
            alive: A boolean representing if the alien is alive or dead.
            velocity_y: An integer representing the current y velocity of the alien.
            jump_strength: An integer representing the amount the alien is jumping.
            gravity: An integer representing the strength of gravity.
            original_y: An integer representing the current y position of the alien.
            on_ground: A boolean representing whether or not the alien is touching the ground.
            jumping: A boolean representing whether or not the alien is jumping.
        """
        self.image = image
        self.rect = image.get_rect()
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

    def update(self):
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

    def animate_alien(self):
        """
        Updates alien's graphic to one of three images to display running and jumping.
        """
        image_sprite = [
            pygame.image.load(
                "image_right_foot.png", "image_left_foot.png", "image_rest.png"
            )
        ]
        clock = pygame.time.Clock()
        value = 0
        image = image_rest
        while self.alive and not self.jumping:
            clock.tick(3)
            if value >= len(image_sprite):
                value = 0
            image = image_right_foot
            time.sleep(0.5)
            image = image_left_foot
            time.sleep(0.5)

    def alien_death(self):
        """
        Updates the alien's status from alive to dead when it falls.
        """
        # How to detect death
        self.alive = False

    def jump(self):
        """
        Makes the alien jumping by changing it's y position.
        """
        if self.on_ground and self.alive:
            self.velocity_y = self.jump_strength
            self.on_ground = False
            self.jumping = True
