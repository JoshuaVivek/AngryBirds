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
from birds import *



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

                    ##########blocks##########
                    
#block images for different health ranges
# Wood block images
wood_images = {
    range(0,1): "None",
    range(1, 1501): "images\wood__(30_0).png",
    range(1501, 3501): "images\wood__(70_30).png",
    range(3501, 5001): "images\wood__(100_70).png"
}

# Stone block images
stone_images = {
    range(0,1): "None",
    range(1, 1501): "images\stone__(30_0).png",
    range(1501, 3501): "images\stone__(70_30).png",
    range(3501, 5001): "images\stone__(100_70).png"
}

# Ice block images
ice_images = {
    range(0,1): "None",
    range(1, 1501): "images\ice__(30_0).png",
    range(1501, 3501): "images\ice__(70_30).png",
    range(3501, 5001): "images\ice__(100_70).png"
}

# assigning coordinates to blocks
block_coordinates = [(50, screen_height - 50), (50, screen_height - 100), (50, screen_height - 150),(50, screen_height - 200),(50, screen_height - 250),(50, screen_height - 300),(screen_width - 100, screen_height -300),(screen_width - 100, screen_height - 250),(screen_width - 100, screen_height - 200),(screen_width - 100, screen_height - 150),(screen_width - 100, screen_height - 100),(screen_width - 100, screen_height - 50)]
block_type = assign_blocks_to_coordinates(block_coordinates) #assigning blocks to coordinates
blocks = list(block_type.values()) #getting blocks from dictionary


# Create the Block objects based on the random block types
block = []

# Iterate over the list and create Block objects
for block_type in blocks:
    if block_type == "wood":
        block1 = Block(block_type="wood_block", max_health = 5000, images=wood_images)
    elif block_type == "stone":
        block1 = Block(block_type="stone_block", max_health = 5000, images=stone_images)
    elif block_type == "ice":
        block1 = Block(block_type="ice_block", max_health = 5000, images=ice_images)
    
    block.append(block1)

               ##########birds##########

# giving coordinates to birds
bird_cooordinates = [(150,screen_height - 50),(250,screen_height - 50),(350,screen_height - 50), (screen_width - 400,screen_height - 50), (screen_width - 300,screen_height - 50),(screen_width - 200,screen_height - 50)] #coordinates of birds
#assigning random birds to coordinates
birds = []
for coord in bird_cooordinates:
    bird = create_random_bird(coord[0], coord[1]) #creating random birds at coordinates
    birds.append(bird)
    
#creating bird_left and bird_right for player1 and player2 respectively
bird_left = AngryBird(bird_type="Red", x=245, y=screen_height - 205, velocity=0, image="None", damage_multiplier=1.0,selected = False) #creating bird for player1
bird_right = AngryBird(bird_type="Red", x=screen_width - 280, y=screen_height - 200, velocity=0, image="None", damage_multiplier=1.0, selected = False) #creating bird for player2

bird_left_owner = 1
bird_right_owner = 2

#displaying the game screen name
pygame.display.set_caption("Angry Birds(Multiplayer)")

# Load images
game_background = pygame.image.load("images\game_background.png").convert()
game_background = pygame.transform.scale(game_background, (screen_width, screen_height))

    ###########slings###########

sling_image1 = pygame.image.load("images\sling_player1.png").convert_alpha()
sling_image2 = pygame.image.load("images\sling_player2.png").convert_alpha()


sling_width = 50
sling_height = 100

sling_image1 = pygame.transform.scale(sling_image1, (sling_width, sling_height))
sling_image2 = pygame.transform.scale(sling_image2, (sling_width, sling_height))

# Sling positions
sling_left_pos = (243, screen_height - sling_height - 100)
sling_right_pos = (screen_width - sling_width - 228, screen_height - sling_height - 100)

# Sling anchor points
sling_left_anchor1 = (sling_left_pos[0] + 15, sling_left_pos[1] + 20)
sling_left_anchor2 = (sling_left_pos[0] + 40, sling_left_pos[1] + 20)

sling_right_anchor1 = (sling_right_pos[0] + 5 , sling_right_pos[1] + 15)
sling_right_anchor2 = (sling_right_pos[0] + 30, sling_right_pos[1] + 20)

#launching the bird
def launch_bird(bird, sling_pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    sling_x, sling_y = sling_pos

    # Calculate drag vector
    dx = sling_x - mouse_x
    dy = sling_y - mouse_y

    # Limit maximum drag distance
    max_drag_distance = 150
    drag_distance = (dx**2 + dy**2)**0.5
    if drag_distance > max_drag_distance:
        scale = max_drag_distance / drag_distance
        dx *= scale
        dy *= scale

    # Launch the bird
    bird.velocity = [dx * 5000, dy * 5000]  # Multiplied for speed tuning
    bird.launched = True
    

player1_score = 0 #player1 score
player2_score = 0 #player2 score
    
# Check collision between bird and blocks
def check_collision(bird, blocks, block_coordinates, current_player):
    global player1_score, player2_score

    bird_rect = bird.image.get_rect(topleft=(bird.x, bird.y))
    for i, blk in enumerate(blocks):
        if blk.is_destroyed():
            continue

        # Skip blocks belonging to current player
        if (current_player == 1 and i < 6) or (current_player == 2 and i >= 6):
            continue

        bx, by = block_coordinates[i]
        block_rect = pygame.Rect(bx, by, 50, 50)

        if bird_rect.colliderect(block_rect):
            # Compute the intersection rect
            overlap = bird_rect.clip(block_rect)

            # Resolve penetration along the smaller axis
            if overlap.width < overlap.height:
                # Horizontal collision
                if bird_rect.centerx < block_rect.centerx:
                    bird.x -= overlap.width
                else:
                    bird.x += overlap.width
                bird.vx *= -bird.restitution
            else:
                # Vertical collision
                if bird_rect.centery < block_rect.centery:
                    bird.y -= overlap.height
                else:
                    bird.y += overlap.height
                bird.vy *= -bird.restitution

            # Update the bird’s stored velocity vector
            bird.velocity = [bird.vx, bird.vy]

            # Damage & scoring
            damage = int(bird.calculate_damage())
            blk.take_damage(damage)
            if current_player == 1:
                player1_score += damage
            else:
                player2_score += damage

            return

        
def check_win_condition(blocks, player1_score, player2_score):
    """Checks if the winning condition is met."""

    player1_blocks_destroyed = all(block.is_destroyed() for block in blocks[:6])
    player2_blocks_destroyed = all(block.is_destroyed() for block in blocks[6:])
    
    if player1_blocks_destroyed and not player2_blocks_destroyed:
        player1_score += 1500  # Bonus points for winning
        if player1_score > player2_score:
            return 1
        elif player1_score < player2_score:
            return 2
        else:
            return 3
    if player2_blocks_destroyed and not player1_blocks_destroyed:
        player2_score += 1500  # Bonus points for winning
        if player2_score > player1_score:
            return 2
        elif player2_score < player1_score:
            return 1
        else:
            return 3
         
    else:
        return 0  # No winner yet

def display_winner(screen, winner_name):
    """Displays the winner's name at the center of the screen."""
    font = pygame.font.Font(None, 72)
    text = font.render(f"{winner_name} wins!", True, (255, 255, 255))  # White color
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)  # Display for 3 seconds
    pygame.quit()
    sys.exit()


#assigning player who is playing first
current_player = 1 #player1 is playing first
bird_active = False #bird is not active at the start

#player score

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 48)

# Game loop
clock = pygame.time.Clock()
running = True
elapsed_time = 0 #time elapsed for the bird to be launched
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False

        birds, bird_left, bird_right, current_player, bird_active = handle_bird_selection(event, birds, sling_left_pos, sling_right_pos, current_player, bird_left, bird_right, screen_height,screen_width,bird_active) #function to handle bird selection and launching

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Allow dragging if clicked on bird_left
            if bird_left and bird_left.get_image() != "None":
                bird_rect = bird_left.image.get_rect(topleft=(bird_left.x, bird_left.y))
                if bird_rect.collidepoint(mouse_pos):
                    bird_left.dragging = True

            # Allow dragging if clicked on bird_right
            if bird_right and bird_right.get_image() != "None":
                bird_rect = bird_right.image.get_rect(topleft=(bird_right.x, bird_right.y))
                if bird_rect.collidepoint(mouse_pos):
                    bird_right.dragging = True


        if event.type == pygame.MOUSEBUTTONUP:
            if bird_left is not None and bird_left.dragging:
                bird_left.dragging = False
                bird_left.launched = True
                bird_left.launch() # Call the launch method to set launch_time
                sling_x, sling_y = sling_left_pos
                pull_x = sling_x - bird_left.x
                pull_y = sling_y - bird_left.y
                bird_left.vx = pull_x * 8
                bird_left.vy = pull_y * 8
                bird_active = True # Bird has been launched

            elif bird_right is not None and bird_right.dragging:
                bird_right.dragging = False
                bird_right.launched = True
                bird_right.launch() # Call the launch method to set launch_time
                sling_x, sling_y = sling_right_pos
                pull_x = sling_x - bird_right.x
                pull_y = sling_y - bird_right.y
                bird_right.vx = pull_x * 8
                bird_right.vy = pull_y * 8
                bird_active = True # Bird has been launched
                
            if bird_left is not None and bird_left.dragging:
                bird_left_owner = 1  # set owner

            elif bird_right is not None and bird_right.dragging:
                bird_right_owner = 2  # set owner


    # Apply physics to launched birds
    dt = clock.get_time() / 1000  # Convert milliseconds to seconds

    if bird_left and bird_left.launched:
        bird_left.apply_physics(dt, screen_height)
        check_collision(bird_left, block, block_coordinates, bird_left_owner)  # Check collision with blocks
    if bird_right and bird_right.launched:
        bird_right.apply_physics(dt, screen_height)
        check_collision(bird_right, block, block_coordinates, bird_right_owner)  # Check collision with blocks

       # Time limit for the bird's flight
       # Time limit for the bird's flight
    TIME_LIMIT = 5

    # Handle bird timeout and player switching
    if bird_left and bird_left.launched and bird_left.launch_time is not None:
        elapsed_time_left = time.time() - bird_left.launch_time
        if elapsed_time_left > TIME_LIMIT:
            bird_left = None
            bird_active = False
            current_player = 2
            elapsed_time_left = 0  # Reset for the next bird

    elif bird_right and bird_right.launched and bird_right.launch_time is not None:
        elapsed_time_right = time.time() - bird_right.launch_time
        if elapsed_time_right > TIME_LIMIT:
            bird_right = None
            bird_active = False
            current_player = 1
            elapsed_time_right = 0  # Reset for the next bird

    elif not bird_left and not bird_right:
        bird_active = False # No bird is currently active

    elif not bird_active:
        # Ready for the next player to select a bird
        pass

    # If dragging, update bird position with mouse
    if bird_left and bird_left.dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        sling_x, sling_y = sling_left_pos
        dx = mouse_x - sling_x
        dy = mouse_y - sling_y
        distance = math.hypot(dx, dy)
        max_distance = 150  # or whatever limit you want
        if distance > max_distance:
            dx = dx * max_distance / distance
            dy = dy * max_distance / distance
        bird_left.x = sling_x + dx
        bird_left.y = sling_y + dy

    if bird_right and bird_right.dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        sling_x, sling_y = sling_right_pos
        dx = mouse_x - sling_x
        dy = mouse_y - sling_y
        distance = math.hypot(dx, dy)
        max_distance = 150
        if distance > max_distance:
            dx = dx * max_distance / distance
            dy = dy * max_distance / distance
        bird_right.x = sling_x + dx
        bird_right.y = sling_y + dy

    # Draw background (static)
    screen.blit(game_background, (0, 0))

    # Draw slings
    screen.blit(sling_image1, sling_left_pos)
    screen.blit(sling_image2, sling_right_pos)

    if bird_left and bird_left.dragging:
        pygame.draw.line(screen, (0, 0, 0), sling_left_anchor1, (bird_left.x +25, bird_left.y + 25), 3)
        pygame.draw.line(screen, (0, 0, 0), sling_left_anchor2, (bird_left.x + 25, bird_left.y + 25), 3)
        draw_trajectory(screen, bird_left, sling_left_pos, screen_height, color=(255, 255, 255))
        
    if bird_right and bird_right.dragging:
        pygame.draw.line(screen, (0, 0, 0), sling_right_anchor1, (bird_right.x + 25, bird_right.y + 25), 3)
        pygame.draw.line(screen, (0, 0, 0), sling_right_anchor2, (bird_right.x + 25, bird_right.y + 25), 3)
        draw_trajectory(screen, bird_right, sling_right_pos, screen_height, color=(255,255,255))


    # Loop through each block and its coordinate
    for i in range(len(blocks)):
        current_block = block[i]  # Get the block
        x, y = block_coordinates[i]  # Get the corresponding coordinate

        image_path = current_block.get_image()  # Get the image path for the block
        if not current_block.is_destroyed():
            if image_path is not None and image_path != "None":
                block_image = pygame.image.load(image_path).convert_alpha()  # Load the image
                # Draw the block image at the (x, y) position
                screen.blit(block_image, (x, y))

    #for each bird in birds, check if the image is not "None" and then draw it
    for bird in birds:
            screen.blit(bird.image, (bird.x, bird.y))
    if bird_left is not None and bird_left.get_image() != "None":
        screen.blit(bird_left.image, (bird_left.x, bird_left.y))
    if bird_right is not None and bird_right.get_image() != "None":
        screen.blit(bird_right.image, (bird_right.x, bird_right.y))
     
     #display who is playing   
    player_text = font.render(f"Next to play : Player {current_player}", True, (173, 216, 230))
    player1_score_text = font.render(f"Score: {player1_score}", True, (173, 216, 230))
    player2_score_text = font.render(f"Score: {player2_score}", True, (173, 216, 230))
    text_rect1 = player1_score_text.get_rect(center=(screen_width // 10,  50))  # Centered at bottom (y=screen_height - 50)
    text_rect2 = player_text.get_rect(center=(screen_width // 2, 50))  # Centered at top (y=50)
    text_rect3 = player2_score_text.get_rect(center=(screen_width - screen_width // 10, 50))  # Centered at bottom (y=screen_height - 50)
    screen.blit(player1_score_text, text_rect1)
    screen.blit(player_text, text_rect2)
    screen.blit(player2_score_text, text_rect3)
    
    winner = check_win_condition(block, player1_score, player2_score)  # Check win condition
    if winner == 1:
        display_winner(screen, player1_name)
    elif winner == 2:
        display_winner(screen, player2_name)
    elif winner == 3:
        display_winner(screen, "It's a draw!")

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()