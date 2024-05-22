import random
import json

class ComboGenerator:
    def __init__(self, combos_file):
        with open(combos_file, 'r') as file:
            self.combos_data = json.load(file)

    def get_highest_level(self):
        highest_level = 0
        for theme in self.combos_data['themes'].values():
            for stratagem in theme:
                level = stratagem['requirements']['level']
                if level > highest_level:
                    highest_level = level
        return highest_level

    def generate_combos(self, min_level, max_level, num_combos):
        combos = []
        available_stratagems = self.get_available_stratagems(min_level, max_level)
        for _ in range(num_combos):
            stratagem = random.choice(available_stratagems)
            combo = {
                'name': stratagem['name'],
                'button_inputs': stratagem['button_inputs']
            }
            combos.append(combo)
        return combos

    def get_available_stratagems(self, min_level, max_level):
        available_stratagems = []
        for stratagems in self.combos_data['themes'].values():
            for stratagem in stratagems:
                if min_level <= stratagem['requirements']['level'] <= max_level:
                    available_stratagems.append(stratagem)
        return available_stratagems