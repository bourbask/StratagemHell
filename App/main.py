import os
import pygame

from configparser import ConfigParser
from configparser import ExtendedInterpolation

from Classes.game import Game
from Classes.menu import Menu
from Classes.end_screen import EndScreen
from Classes.music_player import MusicPlayer

from Config import MUSIC_BASEPATH, SOUNDFONT_PATH, SCREEN_WIDTH, SCREEN_HEIGHT, ROOT_DIR

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("STRATAGEMHELL")

# Initialize font
font = pygame.font.Font(os.path.join(ROOT_DIR, 'Fonts', 'DejaVuSans.ttf'), 25)

# Create instances of the classes
game = Game(screen, font)
menu = Menu(screen, font)
end_screen = EndScreen(screen, font)
music_player = MusicPlayer(music_basepath=MUSIC_BASEPATH, sound_font_path=SOUNDFONT_PATH)
# music_player.play_music_in_loop()

# Define game states
MAIN_MENU = "main_menu"
PLAYING = "playing"
GAME_OVER = "game_over"

# Initial game state
game_state = MAIN_MENU

# Main loop
running = True
while running:
    if game_state == MAIN_MENU:
        menu.display_menu()
        if menu.wait_for_input():
            game_state = PLAYING
            # Start the game when transitioning to PLAYING state
            game.start()  

    elif game_state == PLAYING:
        if game.start():
            game_state = GAME_OVER

    elif game_state == GAME_OVER:
        if end_screen.display_end_screen():
            game_state = MAIN_MENU

    for event in pygame.event.get():  # Handle events outside of game states
        if event.type == pygame.QUIT:
            running = False

# Stop music and quit Pygame
music_player.stop_music()
pygame.quit()
