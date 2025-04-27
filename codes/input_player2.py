import pygame
pygame.init()

def player2(): #function to take player1 name
    
    font = pygame.font.Font(None, 48)
    
    #screen settings
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN flag to keep game in full screen
    screen_width, screen_height = screen.get_size()
    
    # setting a name for game window
    pygame.display.set_caption('Angry Birds(Multiplayer)')   ##we dont need it but just kept for my own intrest
    

    # Load background image
    background2 = pygame.image.load("images\Player2_name_input.png") # Replace backgroung with your image
    background2 = pygame.transform.scale(background2, (screen_width, screen_height))  # Resize to full screen

    input_box = pygame.Rect(505, 469, 530, 59)
    
    #current_background
    current_background = background2

    pygame.key.start_text_input()
    pygame.key.set_text_input_rect(input_box)
    player2_name = ""
    
    running = True
    while running:
        screen.blit(current_background, (0, 0))  # Draw background image
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)  # Input box

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.TEXTINPUT:
                player2_name += event.text

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player2_name = player2_name[:-1]
                if event.key == pygame.K_RETURN:
                    print("Entered:", player2_name)
                    if(player2_name == ""):
                        player2_name = "Player 2"
                    return player2_name
                if event.key == pygame.K_ESCAPE:
                    running = False

        text_surface = font.render(player2_name, True, (128, 0, 128))
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        pygame.display.update()

    pygame.key.stop_text_input()
    pygame.quit()
