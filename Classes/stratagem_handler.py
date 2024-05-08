import random

from combo_generator import ComboGenerator

class StratagemHandler:
    def __init__(self):
        self.generator = ComboGenerator('./Data/combos.json')
        self.combos = []
        self.current_level = 1
        self.current_stratagem_index = 0
        self.score = 0

    def generate_stratagems(self, max_rounds=5):
        max_level_in_file = self.generator.get_highest_level()
        gap = max_level_in_file / max_rounds

        for i in range(max_rounds):
            min_level = int(gap * i)
            max_level = int(gap * (i + 1))
            self.combos.append(self.generator.generate_combos(min_level, max_level, num_combos=10))

    def get_next_stratagem(self):
        # Function to get the next stratagem based on the current level
        if self.current_level == 1:
            # Check if all stratagems in current level have been completed
            if self.current_stratagem_index >= len(self.stratagems[1]):
                self.current_level += 1  # Move to next level
                self.current_stratagem_index = 0  # Reset index for the next level
        elif self.current_level == 2:
            # Similar logic for other levels
            pass
        # Repeat similar logic for other levels

        # Get the next stratagem based on the current level and index
        next_stratagem = self.stratagems[self.current_level][self.current_stratagem_index]
        self.current_stratagem_index += 1
        return next_stratagem

    def check_combo_success(self, combo_inputs, user_inputs):
        # Function to check if the user's inputs match the combo inputs
        return combo_inputs == user_inputs  # Simplified logic for demonstration

    def update_score(self, combo_success):
        # Function to update the score based on combo success
        if combo_success:
            self.score += 1
        else:
            self.score -= 1

    def get_current_level(self):
        # Function to get the current level
        return self.current_level