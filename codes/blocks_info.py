import random
        
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
