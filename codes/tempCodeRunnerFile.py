    block_image = pygame.image.load(image_path).convert_alpha()  # Load the image
        # Draw the block image at the (x, y) position
        screen.blit(block_image, (x, y))