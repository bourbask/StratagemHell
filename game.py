import pygame
import random
import time
import json
from end_screen import end_screen

# Define arrow key constants
UP = pygame.K_z
LEFT = pygame.K_q
DOWN = pygame.K_s
RIGHT = pygame.K_d

# Define level speed constants (in seconds)
LEVEL_SPEED = {
    1: 2.0,
    2: 1.5,
    3: 1.0,
    4: 0.75,
    5: 0.5
}

# Load combos from JSON file
with open('combos.json', 'r') as file:
    combos_data = json.load(file)

# Function to select a random theme and stratagem based on difficulty level
def select_combo(level):
    theme = random.choice(list(combos_data['themes'].keys()))
    stratagem = random.choice(combos_data['themes'][theme])
    return theme, stratagem

# Function to start the game
def start_game(screen, font):
    theme, stratagem = select_combo(1)
    button_inputs = stratagem['button_inputs']
    start_time = time.time()
    chrono_duration = LEVEL_SPEED[1]
    chrono_end = start_time + chrono_duration
    while True:
        screen.fill((255, 255, 255))
        display_text(screen, "Press the following inputs:", 50, 50, font)
        display_text(screen, ", ".join(button_inputs), 300, 200, font)
        display_text(screen, "Theme: {}".format(theme), 50, 100, font)
        display_text(screen, "Level: {}".format(1), 50, 150, font)
        display_text(screen, "Time left: {:.2f}".format(chrono_end - time.time()), 50, 250, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if len(button_inputs) > 0 and event.key == button_inputs[0]:
                    button_inputs.pop(0)
                if len(button_inputs) == 0:
                    print("Combo complete!")
                    if time.time() < chrono_end:
                        return True
                else:
                    print("Wrong input!")
                    return False

        pygame.display.update()


# Function to display text on the screen
def display_text(screen, text, x, y, font, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
