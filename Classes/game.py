import pygame
import random
import time
import json

from Config import SCREEN_WIDTH

# Load level speed from JSON file
with open('./Data/level_speed.json', 'r') as file:
    LEVEL_SPEED = json.load(file)

# Load combos from JSON file
with open('./Data/combos.json', 'r') as file:
    COMBOS_DATA = json.load(file)

# Load key codes from JSON file
with open('./Data/key_codes.json', 'r') as file:
    KEY_CODES_DATA = json.load(file)

# Define color constants
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 255, 0)

class Game:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.theme = None
        self.stratagem = None
        self.button_inputs = []
        self.stratagem_title = None
        self.start_time = None
        self.chrono_duration = None
        self.chrono_end = None
        self.input_colors = [BLACK_COLOR] * len(self.button_inputs)  # Initialize all inputs to black
        self.bar_length = SCREEN_WIDTH - 100  # Length of the time bar
        self.bar_height = 20  # Height of the time bar
        self.bar_color = (0, 255, 0)  # Color of the time bar

    def select_combo(self, level):
        theme = random.choice(list(COMBOS_DATA['themes'].keys()))
        stratagem = random.choice(COMBOS_DATA['themes'][theme])
        return theme, stratagem

    def start_game(self):
        self.theme, self.stratagem = self.select_combo(1)
        self.button_inputs = self.stratagem['button_inputs']
        self.stratagem_title = self.stratagem['name']
        self.start_time = time.time()
        self.chrono_duration = LEVEL_SPEED['1']
        self.chrono_end = self.start_time + self.chrono_duration
        self.draw_time_bar()

        while True:
            self.screen.fill((255, 255, 255))
            self.display_text("Press the following inputs:", 50, 50)
            self.display_text(", ".join(self.button_inputs), 300, 200)
            self.display_text("Stratagem: {}".format(self.stratagem_title), 50, 100)
            self.display_text("Level: {}".format(1), 50, 150)
            self.display_text("Time left: {:.2f}".format(self.chrono_end - time.time()), 50, 250)
            self.display_text("Press M to toggle music", 50, 300)

            if not self.handle_time():
                return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    print(len(self.button_inputs) > 0, event.key == KEY_CODES_DATA[self.button_inputs[0]])
                    if len(self.button_inputs) > 0 and event.key == KEY_CODES_DATA[self.button_inputs[0]]:
                        self.button_inputs.pop(0)
                        print(self.button_inputs, self.input_colors)
                        self.input_colors.append(GREEN_COLOR)
                        if len(self.button_inputs) == 0:
                            print("Combo complete!")
                            self.reset_inputs()
                            return True
                    else:
                        print("Wrong input!")
                        self.reset_inputs()
                        return False

            pygame.display.update()

    def draw_time_bar(self):
        # Calculate remaining time percentage
        remaining_time = max(self.chrono_end - time.time(), 0)
        percentage = remaining_time / self.chrono_duration

        # Calculate width of the bar based on percentage
        bar_width = int(self.bar_length * percentage)

        # Draw the time bar
        pygame.draw.rect(self.screen, self.bar_color, (50, 350, bar_width, self.bar_height))

    def render_inputs(self):
        for i, (input_text, color) in enumerate(zip(self.button_inputs, self.input_colors)):
            self.display_text(input_text, x=300 + i * 50, y=200, color=color)

    def reset_inputs(self):
        self.button_inputs, self.input_colors = self.select_combo(1)  # Reset inputs and colors for the next combo

    def handle_time(self):
        remaining_time = self.chrono_duration - (time.time() - self.start_time)
        if remaining_time <= 0:
            print("Out of time! Game over.")
            return False
        else:
            return True

    def display_text(self, text, x, y, color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
