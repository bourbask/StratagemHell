import pygame

def end_screen(screen, font):
    screen.fill((255, 255, 255))
    display_text(screen, "Game Over", 300, 200, font)
    display_text(screen, "Press ENTER to play again or ESC to quit", 180, 250, font)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

def win_screen(screen, font):
    screen.fill((255, 255, 255))
    display_text(screen, "You Win!", 300, 200, font)
    display_text(screen, "Press ENTER to play again or ESC to quit", 180, 250, font)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

def lose_screen(screen, font):
    screen.fill((255, 255, 255))
    display_text(screen, "You Lose!", 300, 200, font)
    display_text(screen, "Press ENTER to play again or ESC to quit", 180, 250, font)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

def display_text(screen, text, x, y, font, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
