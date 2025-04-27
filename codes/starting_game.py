import pygame

#inititating pygame
pygame.init()
    
#define function start game
def start_game():

    #manage fps
    clock = pygame.time.Clock()
    
    #screen settings
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN flag to keep game in full screen
    screen_width, screen_height = screen.get_size()

    # setting a name for game window
    pygame.display.set_caption('Angry Birds(Multiplayer)')   ##we dont need it but just kept for my own intrest
    
    #starting interface
    background1 = pygame.image.load("images\starting_interface.png")
    background2 = pygame.image.load("images\Player1_name_input.png")

    #making them full screen
    background1 = pygame.transform.scale(background1, (screen_width, screen_height))
    background2 = pygame.transform.scale(background2, (screen_width, screen_height))
    
    #declaring variable current background and setting initial background
    current_background = background1
        
    #####starting the code#######
    running_starting = True
    while running_starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running_starting = False #we are in full screen so no wrong button
                if event.key == pygame.K_RETURN:  # Enter key is pressed
                        return
                    
        #### Draw the current background and updating screen
        screen.blit(current_background, (0, 0))
        pygame.display.flip()
             