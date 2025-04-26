import pygame
pygame.init()

def player1(): #function to take player1 name
    
    font = pygame.font.Font(None, 48)
    
    #screen settings
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN flag to keep game in full screen
    screen_width, screen_height = screen.get_size()

    # Load background image
    background2 = pygame.image.load("images\Player1_name_input.png") # Replace backgroung with your image
    background2 = pygame.transform.scale(background2, (screen_width, screen_height))  # Resize to full screen

    input_box = pygame.Rect(505, 469, 530, 59)
    
    #current_background
    current_background = background2

    pygame.key.start_text_input()
    pygame.key.set_text_input_rect(input_box)
    player1_name = ""
    
    running = True
    while running:
        screen.blit(current_background, (0, 0))  # Draw background image
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)  # Input box

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.TEXTINPUT:
                player1_name += event.text

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player1_name = player1_name[:-1]
                if event.key == pygame.K_RETURN:
                    print("Entered:", player1_name)
                    return player1_name
                if event.key == pygame.K_ESCAPE:
                    running = False

        text_surface = font.render(player1_name, True, (128, 0, 128))
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        pygame.display.update()

    pygame.key.stop_text_input()
    pygame.quit()
