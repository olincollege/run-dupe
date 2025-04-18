"""
Add docstring
"""

import pygame
import time

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


class Alien:
    """
    Add docstring
    """

    def _init_(self):
        """
        Add docstring
        """
        self.alive = False

    def animate_alien(self):
        """
        Add docstring
        """
        while self.alive and not self.jumping:
            image = right_foot
            time.sleep(0.5)
            image = left_foot
            time.sleep(0.5)
        image = rest

    def alien_death(self):
        """
        Add docstring
        """

    def jump(self):
        """
        Add docstring
        """
        while self.alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.alive = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                dude.y -= 1
                self.jumping = True
            elif dude.y < 220:
                dude.y += 1
                self.jumping = True
        pygame.display.flip()
