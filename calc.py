import pygame

screen = pygame.display.set_mode((400, 400))

calc_running = True

while calc_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calc_running = False