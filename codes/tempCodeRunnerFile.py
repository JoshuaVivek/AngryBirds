
# Example coordinates (12 positions)
coordinates = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
    (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)
]

# Generate the block assignments for the coordinates
block_assignments = assign_blocks_to_coordinates(coordinates)

# Print the resulting block assignments
print("Block assignments:", block_assignments)
