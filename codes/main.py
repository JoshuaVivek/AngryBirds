#importing all standard libraries which can be used
import pygame
import numpy as np
import random
import math
import sys
import os
import time

#importing my modules
from starting_game import *
from input_player1 import *
from input_player2 import *
from p1_vs_p2 import *

                          ######## main file ###########
                          
start_game() #used to start game and ask player details and take you into game

player1_name = player1() #function to take player1 name
  
print("Player 1 name:", player1_name) #print player1 name

player2_name = player2() #function to take player2 name

print("Player 2 name:", player2_name) #print player2 name

player1_vs_player2(player1_name, player2_name) #function to show player1 vs player2 screen

        ### let's start the game screen###
        

# Initialize Pygame
pygame.init()        

# Full screen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Angry Birds(Multiplayer)")

# Load images
game_background = pygame.image.load("images\game_background.png").convert()
game_background = pygame.transform.scale(game_background, (screen_width, screen_height))

sling_image1 = pygame.image.load("images\sling_player1.png").convert_alpha()
sling_image2 = pygame.image.load("images\sling_player2.png").convert_alpha()

sling_width = 50
sling_height = 100

sling_image1 = pygame.transform.scale(sling_image1, (sling_width, sling_height))
sling_image2 = pygame.transform.scale(sling_image2, (sling_width, sling_height))

# Sling positions
sling_left_pos = (243, screen_height - sling_height - 100)
sling_right_pos = (screen_width - sling_width - 228, screen_height - sling_height - 100)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False

    # Draw background (static)
    screen.blit(game_background, (0, 0))
    
    # Draw slings
    screen.blit(sling_image1, sling_left_pos)
    screen.blit(sling_image2, sling_right_pos)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()