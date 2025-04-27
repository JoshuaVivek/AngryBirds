#importing libraries
import pygame

pygame.init()

def player1_vs_player2(player1_name, player2_name):
    # Full screen display
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Use (0, 0) for full screen
    pygame.display.set_caption('Angry Birds(Multiplayer)')
    screen_width, screen_height = screen.get_size()

    # Load background and scale it to full screen
    background = pygame.image.load('images\player1vsplayer2.png')
    background = pygame.transform.scale(background, (screen_width, screen_height))  # Resize to full screen


    # Choose font
    font = pygame.font.SysFont('gabriola', 100)  # Bigger font for full screen

    # Render text
    player1_text = font.render(player1_name, True, (51, 153, 255))
    player2_text = font.render(player2_name, True, (255, 51, 51))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Start the game or transition to the next screen
                print("Starting game...")
                return

        # Draw background
        screen.blit(background, (0, 0))

        # Draw texts at custom positions
        screen.blit(player1_text, (100, screen_height//2 - 50))         # Left side for player 1
        screen.blit(player2_text, (screen_width - 400, screen_height//2 - 50))  # Right side for player 2

        pygame.display.flip()

    pygame.quit()
