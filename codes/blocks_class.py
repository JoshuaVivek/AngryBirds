import random

class Block:
    def __init__(self, block_type, max_health, images, damage_multiplier=1.0):
        """
        Initialize a block.

        block_type : Type of the block ("wood", "stone", "glass").
        max_health: Maximum health of the block.
        images: A dictionary mapping health ranges to image paths.
                    
        """
        self.block_type = block_type
        self.max_health = max_health
        self.current_health = max_health
        self.images = images
        self.damage_multiplier = damage_multiplier

    def take_damage(self, damage):
        """
        Reduce the block's health by the specified damage amount.

        damage: Amount of damage taken.
        """
        self.current_health = max(0, self.current_health - damage) #we should not go below 0 health

    def get_image(self):
        """
        Get the image representing the block based on its current health.

        :return: Path to the image file.
        """
        for health_range, image in self.images.items():
            if self.current_health in health_range:
                return image
        return None  # Return None if no image matches the current health(will not happen)

    def is_destroyed(self):
        """
        Check if the block is destroyed.

        :return: True if the block's health is 0, False otherwise.
        """
        return self.current_health == 0
        
# Function to generate symmetric block assignments for coordinates
def assign_blocks_to_coordinates(coordinates):
    
    block_types = ["wood", "stone", "ice"]
    # Check if we have exactly 12 coordinates
  
    # Generate 6 random block types 
    block_pair_list = random.sample(block_types * 6, 6)  # Pick 6 random block types (any number of each)
    random.shuffle(block_pair_list)  # Shuffle to randomize the order

    # Create the dictionary for coordinates (assign blocks symmetrically)
    block_assignments = {}

    # Assign blocks to symmetric coordinates
    for i in range(6):
        block_assignments[coordinates[i]] = block_pair_list[i]
        block_assignments[coordinates[11 - i]] = block_pair_list[i]

    return block_assignments

