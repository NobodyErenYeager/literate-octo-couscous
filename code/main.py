import pygame
import sys

pygame.init()
# WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WINDOW_WIDTH, WINDOW_HEIGHT = 1280/1.5, 720/1.5
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Asteroid Shooter")

ship_surf = pygame.image.load('../graphics/ship.png').convert_alpha()
bg_surf = pygame.image.load('../graphics/background.png').convert()

font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, "white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0,0,0,))
    display_surface.blit(bg_surf, (0, 0))
    display_surface.blit(ship_surf, (300/1.5, 500/1.5))
    display_surface.blit(text_surf, (500/1.5, 200/1.5))

    pygame.display.update()
