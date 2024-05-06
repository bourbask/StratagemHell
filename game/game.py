import pygame
from end_screen import EndScreen
from scoreboard import Scoreboard
from combo_manager import ComboManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stratagem Hell")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.scoreboard = Scoreboard()
        self.combo_manager = ComboManager()
        self.end_screen = EndScreen()

        self.running = True

    def start(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

        self.end()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Update game logic here
        self.combo_manager.update()
        if self.combo_manager.is_game_over():
            self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        self.scoreboard.display(self.screen, self.font)
        self.combo_manager.display(self.screen, self.font)
        pygame.display.flip()
        self.clock.tick(60)

    def end(self):
        self.end_screen.display(self.screen, self.font)
        pygame.display.flip()
        pygame.time.wait(2000)  # Delay before quitting
        pygame.quit()
