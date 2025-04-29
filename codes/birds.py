import random
import pygame
import time

class AngryBird:
    def __init__(self, bird_type, x, y, velocity, image, damage_multiplier,selected=False):

        self.bird_type = bird_type
        self.x = x
        self.y = y
        self.velocity = [0, 0]  # Initial velocity is a tuple (vx, vy)
        self.image = image
        self.damage_multiplier = damage_multiplier
        self.dragging = False
        self.launched = False
        self.gravity = 400  
        self.restitution = 0.5  # coefficient of restitution
        self.min_velocity = 500  # Minimum velocity to be considered launched
        self.vx = self.velocity[0]  # Initial horizontal velocity
        self.vy = self.velocity[1]
        self.launch_time = None  # Add a timestamp for when the bird is launched


    def calculate_damage(self):
        """
        Calculate the damage dealt by the bird based on its velocity.

        """
        return self.damage_multiplier * (self.vx ** 2 + self.vy ** 2) ** 0.5

    def update_position(self, new_x, new_y):
        """
        Update the bird's position
        """
        #update the positions
        self.x = new_x
        self.y = new_y
    def update_velocity(self, new_velocity):
        """
        Update the bird's velocity.

        new_velocity: New velocity of the bird
        """
        self.velocity = new_velocity
    def get_image(self):
        """
        Get the image of the bird.

        return: Image of the bird
        """
        return self.image  
    def get_position(self):
        """
        Get the current position of the bird.

        :return: Tuple (x, y) representing the bird's position
        """
        return self.x, self.y
    def get_bird_type(self):
        """
        Get the type of the bird.

        :return: Type of the bird
        """
        return self.bird_type
    def get_velocity(self):
        """
        Get the velocity of the bird.
        return: Velocity of the bird
        """
        return self.velocity
    
    def select(self):
        """Marks the bird as selected."""
        self.selected = True

    def deselect(self):
        """Marks the bird as deselected."""
        self.selected = False
        
    def apply_physics(self, dt, screen_height):
        if self.launched:
            gravity = 400  # pixels per second squared (adjustable)
            self.vy += gravity * dt  # Gravity affects y-velocity
            self.x += self.vx * dt
            self.y += self.vy * dt

            # Bounce off the ground
            if self.y >= screen_height - self.image.get_height():
                self.y = screen_height - self.image.get_height()
                self.vy = -self.vy * 0.5  # Lose some energy on bounce
                self.vx *= 0.7  # Slow down horizontally
                if abs(self.vy) < 50:  # Stop bouncing when almost still
                    self.vy = 0 
    def launch(self):
        """Launch the bird and record the launch time."""
        self.launched = True
        self.launch_time = time.time()  # Record the current time when the bird is launched


        
def create_random_bird(x, y):
        """
        Create a random AngryBird at the specified position.

        x: x-coordinate of the bird
        y: y-coordinate of the bird

        return: An instance of AngryBird with random type and properties
        """
        # Define bird types and their properties
        bird_types = {
            "Red": {"damage_multiplier": 1.0},
            "Blue": {"damage_multiplier": 1.5},
            "Chuck": {"damage_multiplier": 2.0},
            "Bomb": {"damage_multiplier": 2.5}
        }

        # Load images for each bird type (assuming images are available in a dictionary)
        bird_images = {
            "Red": pygame.image.load("images/red.png").convert_alpha(),
            "Blue": pygame.image.load("images/blue.png").convert_alpha(),
            "Chuck": pygame.image.load("images/chuck.png").convert_alpha(),
            "Bomb": pygame.image.load("images/bomb.png").convert_alpha()
        }
        #Creates a random AngryBird at the specified position.
        
        bird_type = random.choice(list(bird_types.keys()))
        velocity = 0  # Initial velocity is 0
        image = bird_images[bird_type]
        damage_multiplier = bird_types[bird_type]["damage_multiplier"]
        return AngryBird(bird_type, x, y, velocity, image, damage_multiplier, selected=False)

def handle_bird_selection(event, birds, sling_left_pos, sling_right_pos, current_player, bird_left, bird_right,screen_height,screen_width,bird_active):
    if bird_active:
        return birds, bird_left, bird_right, current_player, bird_active  # Do not allow new selections if a bird is already active
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        for i, bird in enumerate(birds):
            bird_rect = bird.image.get_rect(topleft=(bird.x, bird.y))
            if bird_rect.collidepoint(mouse_pos):
                # Check if the bird is selectable by the current player
                if (current_player == 1 and bird.x < screen_width // 2) or (current_player == 2 and bird.x >= screen_width // 2):
                    
                    # Deselect any previously selected bird
                    for b in birds:
                        b.deselect()
                    
                    bird.select()  # Select the clicked bird
                    selected_bird_index = i
                    # Move the selected bird to the appropriate sling
                    if current_player == 1:
                        x, y = bird.get_position()
                        bird.update_position(245, screen_height - 205)  # Move to player 1's sling position
                        bird_left = bird #update the bird_left
                        birds[i] = create_random_bird(x, y) #creating random bird at the coordinates
                        current_player = 2 #switch player
                    else:
                        x, y = bird.get_position()
                        bird.update_position(screen_width - 280, screen_height - 200)  # Move to player 2's sling position
                        bird_right = bird #update the bird_right
                        birds[i] = create_random_bird(x, y) #creating random bird at the coordinates
                        current_player = 1 #switch player
                    bird.update_velocity(0)
                    bird_active = True  # Mark the bird as active
                    break  # Only one bird can be selected per click

    return birds, bird_left, bird_right,current_player, bird_active  # Return the updated birds list, selected bird, and current player

