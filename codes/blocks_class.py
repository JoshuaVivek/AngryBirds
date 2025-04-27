class Block:
    def __init__(self, block_type, max_health, images):
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


# Example usage
if __name__ == "__main__":
    # Define images for different health ranges
    wood_images = {
        range(0, 30): "wood_broken.png",
        range(30, 70): "wood_damaged.png",
        range(70, 100): "wood_normal.png"
    }

    # Create a wood block
    wood_block = Block(block_type="wood", max_health=100, images=wood_images)

    # Simulate damage and print the corresponding image
    print("Initial image:", wood_block.get_image())
    wood_block.take_damage(30)
    print("After 30 damage:", wood_block.get_image())
    wood_block.take_damage(50)
    print("After 50 more damage:", wood_block.get_image())
    print("Is block destroyed?", wood_block.is_destroyed())