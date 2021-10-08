import pygame

calc_width = 400
calc_height = 400

screen = pygame.display.set_mode((calc_width, calc_height))


class Button:
    def __init__(self, pos, func):
        self.size = calc_width // 4
        self.pos = (pos[0] * self.size, pos[1] * self.size)
        self.func = func

        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

    def visualisation(self):
        screen.blit(self.surface, self.pos)


test_button = Button([2, 2], 1)

calc_running = True

while calc_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calc_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)

    test_button.visualisation()

    pygame.display.update()
    pygame.time.delay(50)