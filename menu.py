import pygame

# Function to display main menu
def main_menu(screen, font):
    screen.fill((255, 255, 255))
    display_text(screen, "Welcome to Stratagem Hell!", 50, 50, font)
    display_text(screen, "Press SPACE to start or Q to quit", 50, 150, font)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Function to display text on the screen
def display_text(screen, text, x, y, font, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
