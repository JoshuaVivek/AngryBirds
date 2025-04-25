#This module contains functions and details for start of the game

#importing all standard libraries which can be used
import pygame
import numpy as np
import random
import math
import sys
import os
import time

#define function start game
def start_game():
    #inititating pygame
    pygame.init()
    
    #manage fps
    clock = pygame.time.Clock()
    
    #screen settings
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN flag to keep game in full screen
    screen_width, screen_height = screen.get_size()

    # setting a name for game window
    pygame.display.set_caption('Angry Birds(Multiplayer)')
    
    #starting interface
    background1 = pygame.image.load("images\starting_interface.png")
    background2 = pygame.image.load("images\Player1_name_input.png")
    background3 = pygame.image.load("images\Player2_name_input.png")
    
    #making them full screen
    background1 = pygame.transform.scale(background1, (screen_width, screen_height))
    background2 = pygame.transform.scale(background2, (screen_width, screen_height))
    background3 = pygame.transform.scale(background3, (screen_width, screen_height))
    
    #declaring variable current background 
    current_background = background1
    
    #starting the code
    running_starting = True
    while running_starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if press on wrong at top
                running_starting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key is pressed
                    if current_background == background1:
                        pygame.time.delay(250)
                        current_background = background2
                    else:
                        current_background = background1

        # Draw the current background and updating screen
        screen.blit(current_background, (0, 0))
        pygame.display.flip()
            
    # Setting initial background
    current_background = background1
    
    #enter names
    
    #giving a interface player1 vs player2
     