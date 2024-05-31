import os
import pygame

from Config import ROOT_DIR, BLACK_COLOR

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.fontTitle = pygame.font.Font(os.path.join(ROOT_DIR, 'Fonts', 'Swiss721Extended-Bold.otf'), 46)

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        self.display_text("STRATAGEMHELL", 170, 150, BLACK_COLOR, self.fontTitle)
        self.display_text("Press SPACE to start or Q to quit", 200, 250)
        pygame.display.update()

    def wait_for_input(self):
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

    def display_text(self, text, x, y, color=BLACK_COLOR, font=None):
        if font != None:
            text_surface = font.render(text, True, color)
        else:
            text_surface = self.font.render(text, True, color)

        self.screen.blit(text_surface, (x, y))
