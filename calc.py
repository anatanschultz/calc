import pygame

mouse_pos = pygame.Rect(-100, -100, 1, 1)

calc_width = 400
calc_height = 400

screen = pygame.display.set_mode((calc_width, calc_height))


class Button:
    def __init__(self, pos, func):
        self.size = calc_width // 4
        self.pos = (pos[0] * self.size, pos[1] * self.size)
        self.func = func

        self.surface = pygame.Surface((self.size, self.size))
        self.rect = pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))

    def visualisation(self, pos):
        screen.blit(self.surface, self.rect)
        if self.rect.colliderect(pos):
            self.surface.fill((255, 0, 0))
        else:
            self.surface.fill((255, 255, 255))


buttons = []
for x in range(4):
    for y in range(4):
        buttons.append(Button([x, y], 1))

calc_running = True

while calc_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calc_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.Rect(pygame.mouse.get_pos()[0],
                                        pygame.mouse.get_pos()[1],
                                        1,
                                        1)
                print(mouse_pos)

    for i in buttons:
        i.visualisation(mouse_pos)

    pygame.display.update()
    pygame.time.delay(50)