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
    base_font =pygame.font.Font(None,48)
    player1_name = ""
    player2_name =""
    
    #screen settings
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN flag to keep game in full screen
    screen_width, screen_height = screen.get_size()

    # setting a name for game window
    pygame.display.set_caption('Angry Birds(Multiplayer)')   ##we dont need it but just kept for my own intrest
    
    #starting interface
    background1 = pygame.image.load("images\starting_interface.png")
    background2 = pygame.image.load("images\Player1_name_input.png")
    background3 = pygame.image.load("images\Player2_name_input.png")
    
    #making them full screen
    background1 = pygame.transform.scale(background1, (screen_width, screen_height))
    background2 = pygame.transform.scale(background2, (screen_width, screen_height))
    background3 = pygame.transform.scale(background3, (screen_width, screen_height))
    
    #declaring variable current background and setting initial background
    current_background = background1
    
    #info about input box
    input_box = pygame.Rect(505, 469, 530, 59)
        
    #####starting the code#######
    running_starting = True
    while running_starting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running_starting = False #we are in full screen so no wrong button
                if event.key == pygame.K_RETURN:  # Enter key is pressed
                    if current_background == background1:
                        pygame.time.delay(250)
                        current_background = background2

        #### Draw the current background and updating screen
        screen.blit(current_background, (0, 0))
        pygame.display.flip()
            
        #enter names
    
         #giving a interface player1 vs player2
     