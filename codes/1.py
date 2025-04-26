import pygame
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Text Input with Background")
font = pygame.font.Font(None, 48)

# Load background image
background = pygame.image.load("images\Player1_name_input.png")  # <-- Your image file here
background = pygame.transform.scale(background, screen.get_size())  # Resize to full screen

input_box = pygame.Rect(505, 469, 530, 59)
input_text = ""

pygame.key.start_text_input()
pygame.key.set_text_input_rect(input_box)

running = True
while running:
    screen.blit(background, (0, 0))  # Draw background image
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)  # Input box

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.TEXTINPUT:
            input_text += event.text

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            if event.key == pygame.K_RETURN:
                print("Entered:", input_text)
                input_text = ""
            if event.key == pygame.K_ESCAPE:
                running = False

    text_surface = font.render(input_text, True, (128, 0, 128))
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    pygame.display.update()

pygame.key.stop_text_input()
pygame.quit()
