import pygame
import game
import menu
import end_screen

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stratagem Hell")

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Main loop
running = True
while running:
    if menu.main_menu(screen, font):
        game.start_game(screen, font)
    else:
        running = end_screen.end_screen(screen, font)
