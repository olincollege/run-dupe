"""
Add docstring
"""

# class game (moves the tunnel)
#     init
#         frame_rate
#         level
# def move_tunnel
#     left/right arrow key + space bar moves to the opposite side of the tunnel
#             ORRRR
#     holding down arrow key orients the angle of turning of the tunnel
#     changes orientation of the tunnel such that the alien upright
#     space bar = screen shifts down and then back up
#     left arrow = right
#     right arrow = left
# def update_level
#     alien crosses previous level, update to next
# def progress_tunnel
#     move tunnel forward at a constant speed
#     view gets larger when approaching part of the tunnel
import pygame
import start_screen
import alien
import tunnel


class Game:
    """
    Add docstring
    """

    def __init__(self):
        """
        Add docstring
        """
        pygame.init()
        # Make mouse visible
        pygame.mouse.set_visible(True)

        # Create display window
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.platforms = []
        self.alien = Alien(x, y)
        self.platforms = []
        self.start_screen = True
        self.run = False

    def main_loop(self):
        # Load and resize start button image
        start_img = pygame.transform.scale_by(
            pygame.image.load("start_button.png").convert_alpha(), 0.1
        )
        start_button = start_screen.Button(300, 300, start_img)
        while self.start_screen:
            self.screen.fill((0, 0, 0))
            # Create start screen
            start_screen.draw_start(self.alien)
            if not start_screen.Button.draw(self.screen):
                self.start_screen = False
                self.run = True

        while self.run:
            # Event handler
            for event in pygame.event.get():
                # Key press
                if event.type == pygame.KEYDOWN:
                    self.alien.press_keys(pygame.key.get_pressed())
                # Quit game
                if event.type == pygame.QUIT:
                    self.run = False

            # Update platforms for alien
            self.alien.update(self.platforms)

            # Draw everything
            self.screen.fill(0, 0, 0)
            pygame.Rect(self.screen)

            pygame.display.update()

            # Set framerate
            self.clock.tick(60)
        pygame.quit

    def update_level(self):
        """
        Add docstring
        """
        pass
