alien = Alien(#where he's at)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        alien.jump()
    alien.update()
    screen.fill((30, 30, 30))
    alien.draw(screen)
    pygame.display.flip()
