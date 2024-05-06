import pygame
import game
import menu
import end_screen
from music_player import play_music_in_loop

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stratagem Hell")

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Play music in a loop
play_music_in_loop()

# Main loop
running = True
while running:
    if menu.main_menu(screen, font):
        game.start_game(screen, font)
    else:
        running = end_screen.end_screen(screen, font)

# Quit Pygame
pygame.quit()
