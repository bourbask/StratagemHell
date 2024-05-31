import os
import pygame
import time
import json
import random
from Classes.end_screen import EndScreen
# from scoreboard import Scoreboard
from Classes.combo_generator import ComboGenerator
from Config import SCREEN_WIDTH, WHITE_COLOR, BLACK_COLOR, MARGIN_WIDTH, MARGIN_HEIGHT, ROOT_DIR

# Load level speed from JSON file
with open(os.path.join(ROOT_DIR, 'Data/level_speed.json'), 'r') as file:
    LEVEL_SPEED = json.load(file)

# Load key codes from JSON file
with open(os.path.join(ROOT_DIR, 'Data/key_codes.json'), 'r') as file:
    KEY_CODES_DATA = json.load(file)

# Load key icons from JSON file
with open(os.path.join(ROOT_DIR, './Data/keys_icons.json'), 'r', encoding='utf-8') as file:
    KEY_ICONS_DATA = json.load(file)

class Game:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.fontArrows = pygame.font.Font(os.path.join(ROOT_DIR, 'Fonts', 'DejaVuSans-Bold.ttf'), 36)
        # self.scoreboard = Scoreboard()
        self.end_screen = EndScreen(screen, font)
        self.combo_generator = ComboGenerator(os.path.join(ROOT_DIR, 'Data/combos.json'))
        self.current_combo_index = 0
        self.combos = []
        self.start_time = None
        self.chrono_duration = None
        self.chrono_end = None
        self.bar_length = SCREEN_WIDTH - 100  # Length of the time bar
        self.bar_height = 20  # Height of the time bar
        self.bar_color = (0, 255, 0)  # Color of the time bar

    def start(self):
        running = True
        while running:
            self.reset_game()
            running = self.run_game()
            if not running:
                break
            self.end_screen.display(self.screen, self.font, "Game Over. Press R to Retry, Q to Quit.")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        running = True
                    elif event.key == pygame.K_q:
                        running = False

        pygame.quit()

    def reset_game(self):
        self.current_combo_index = 0
        self.combos = self.combo_generator.generate_combos(1, 5, 10)  # Generate 10 combos with levels between 1 and 5
        self.start_time = time.time()
        self.chrono_duration = LEVEL_SPEED['1']
        self.chrono_end = self.start_time + self.chrono_duration

    def run_game(self):
        while True:
            self.screen.fill(WHITE_COLOR)
            self.display_layout([MARGIN_WIDTH, MARGIN_HEIGHT])

            if not self.handle_time():
                return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if not self.handle_combo_input(event.key):
                        return False  # Return False if combo input is incorrect

                    if not self.handle_general_keys(event.key):
                        return False  # Return False if general key handling fails

            pygame.display.update()

    def display_layout(self, margins):
        self.display_general_controls(margins)
        self.display_game_info([margins[0], margins[1] + 100])
        self.display_combo_input([margins[0], margins[1] + 200])

    def display_combo_input(self, position):
        self.display_text("Press the following inputs:", position[0], position[1])
        # current_combo = self.combos[self.current_combo_index]
        # self.display_text(", ".join(current_combo['button_inputs']), position[0] + 150, position[1] + 50)
        current_combo = self.combos[self.current_combo_index]
        icons = [KEY_ICONS_DATA[btn] for btn in current_combo['button_inputs']]
        self.display_text(" ".join(icons), position[0] + 150, position[1] + 50, BLACK_COLOR, self.fontArrows)

    def display_general_controls(self, position):
        self.display_text("Press P to resume game", position[0], position[1])
        self.display_text("Press M to toggle music", position[0] + 300, position[1])
        self.draw_time_bar(position)

    def display_game_info(self, position):
        self.display_text("Stratagem: {}".format(self.combos[self.current_combo_index]['name']), position[0], position[1])
        self.display_text("Level: {}".format(1), position[0], position[1] + 50)

    def handle_combo_input(self, key):
        current_combo = self.combos[self.current_combo_index]
        if len(current_combo['button_inputs']) > 0 and key == KEY_CODES_DATA[current_combo['button_inputs'][0]]:
            current_combo['button_inputs'].pop(0)
            if len(current_combo['button_inputs']) == 0:
                self.current_combo_index += 1
                if self.current_combo_index >= len(self.combos):
                    return True  # All combos completed
                return True  # Combo input is correct
        elif key in [pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d]:
            # Wrong input for the combo
            return False  # Combo input is incorrect

        return True  # No relevant combo input event

    def handle_general_keys(self, key):
        if key == pygame.K_r:
            # Resume game
            return True
        elif key == pygame.K_m:
            # Mute/unmute music
            return True
        # Add more general key handling logic as needed

        return True  # No relevant general key event

    def draw_time_bar(self, position):
        # Calculate remaining time percentage
        remaining_time = max(self.chrono_end - time.time(), 0)
        percentage = remaining_time / self.chrono_duration

        # Calculate width of the bar based on percentage
        bar_width = int(self.bar_length * percentage)

        # Draw the time bar
        pygame.draw.rect(self.screen, self.bar_color, (position[0], position[1] + 350, bar_width, self.bar_height))

    def handle_time(self):
        remaining_time = self.chrono_duration - (time.time() - self.start_time)
        if remaining_time <= 0:
            print("Out of time! Game over.")
            return False
        else:
            return True

    def display_text(self, text, x, y, color=BLACK_COLOR, font=None):
        if font != None:
            text_surface = font.render(text, True, color)
        else:
            text_surface = self.font.render(text, True, color)

        self.screen.blit(text_surface, (x, y))
