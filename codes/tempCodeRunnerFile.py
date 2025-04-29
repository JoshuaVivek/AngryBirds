    if blk.is_destroyed():
            continue

        # Determine if this block belongs to the opponent
        if (current_player == 1 and i >= len(blocks) // 2) or (current_player == 2 and i < len(blocks) // 2):
            block_x, block_y = block_coordinates[i]
            block_rect = pygame.Rect(block_x, block_y, 50, 50)

            if bird_rect.colliderect(block_rect):
                damage = bird.calculate_damage()
                blk.take_damage(damage)

                if current_player == 1:
                    player1_score += int(damage)
                else:
                    player2_score += int(damage)

                bird.vx *= -bird.restitution
                bird.vy *= -bird.restitution
                return