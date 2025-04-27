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
from blocks_class import *
from blocks_info import *


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

#block images for different health ranges
# Wood block images
wood_images = {
    range(1, 31): "images\wood__(30_0).png",
    range(32, 71): "images\wood__(70_30).png",
    range(72, 101): "images\wood__(100_70).png"
}

# Stone block images
stone_images = {
    range(1, 31): "images\stone__(30_0).png",
    range(32, 71): "images\stone__(70_30).png",
    range(72, 101): "images\stone__(100_70).png"
}

# Ice block images
ice_images = {
    range(1, 31): "images\ice__(30_0).png",
    range(32, 71): "images\ice__(70_30).png",
    range(72, 101): "images\ice__(100_70).png"
}

# assigning coordinates to blocks
coordinates = [(50, screen_height - 50), (50, screen_height - 100), (50, screen_height - 150),(50, screen_height - 200),(50, screen_height - 250),(50, screen_height - 300),(screen_width - 100, screen_height -300),(screen_width - 100, screen_height - 250),(screen_width - 100, screen_height - 200),(screen_width - 100, screen_height - 150),(screen_width - 100, screen_height - 100),(screen_width - 100, screen_height - 50)]
block_type = assign_blocks_to_coordinates(coordinates) #assigning blocks to coordinates
blocks = list(block_type.values()) #getting blocks from dictionary


# Create the Block objects based on the random block types
block = []

# Iterate over the list and create Block objects
for block_type in blocks:
    if block_type == "wood":
        block1 = Block(block_type="wood_block", max_health=100, images=wood_images)
    elif block_type == "stone":
        block1 = Block(block_type="stone_block", max_health=100, images=stone_images)
    elif block_type == "ice":
        block1 = Block(block_type="ice_block", max_health=100, images=ice_images)
    
    block.append(block1)

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
    
    # Loop through each block and its coordinate
    for i in range(len(blocks)):
        current_block = block[i]  # Get the block
        x, y = coordinates[i]  # Get the corresponding coordinate
        
        image_path = current_block.get_image()  # Get the image path for the block
        block_image = pygame.image.load(image_path).convert_alpha()  # Load the image
        
        # Draw the block image at the (x, y) position
        screen.blit(block_image, (x, y))
        
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()