import pygame
import game

# Function to display end screen
def end_screen(screen, font):
    screen.fill((255, 255, 255))
    game.display_text(screen, "Game Over", 300, 200, font)
    game.display_text(screen, "Press R to retry, Q to quit or M for main menu", 150, 250, font)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_m:
                    return False
