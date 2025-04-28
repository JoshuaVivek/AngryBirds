import random
import pygame

class AngryBird:
    def __init__(self, bird_type, x, y, velocity, image, damage_multiplier,selected=False):
        """
        Initialize an AngryBird.

        bird_type: Type of the bird (e.g., "Red", "Blue", "Chuck", "Bomb")
        x: Initial x-coordinate position of the bird
        y: Initial y-coordinate position of the bird
        velocity: Initial velocity of the bird
        image: Image representation of the bird
        damage_multiplier: Damage multiplier specific to the bird type
        """
        self.bird_type = bird_type
        self.x = x
        self.y = y
        self.velocity = velocity
        self.image = image
        self.damage_multiplier = damage_multiplier

    def calculate_damage(self):
        """
        Calculate the damage dealt by the bird based on its velocity.

        """
        return self.velocity * self.damage_multiplier

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

def handle_bird_selection(event, birds, sling_left_pos, sling_right_pos, current_player, bird_left, bird_right,screen_height,screen_width):
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
                    break  # Only one bird can be selected per click

    return birds, bird_left, bird_right,current_player
