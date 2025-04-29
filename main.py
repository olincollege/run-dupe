"""_summary_"""

from game import Game

if __name__ == "__main__":
    game = Game()
    game.main_loop()

# import button

# pygame.init()
# pygame.mouse.set_visible(True)

# # Create display window
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# # Load and resize start button image
# start_img = pygame.transform.scale_by(
#     pygame.image.load("start_button.png").convert_alpha(), 0.1
# )
# start_button = start_screen.Button(300, 300, start_img)

# run = True
# while run:

#     screen.fill((0, 0, 0))

#     # Draw start button
#     if start_button.draw(screen):
#         # start game
#         print("start game")
#     # Event handler
#     for event in pygame.event.get():
#         # Quit game
#         if event.type == pygame.QUIT:
#             run = False

#     pygame.display.update()
# pygame.quit

# # alien = Alien("where he's at")
# #     keys = pygame.key.get_pressed()
# #     if keys[pygame.K_SPACE]:
# #         alien.jump()
# #     alien.update()
# #     screen.fill((30, 30, 30))
# #     alien.draw(screen)
# #     pygame.display.flip()
