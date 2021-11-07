import pygame
pygame.font.init()

mouse_pos = pygame.Rect(-100, -100, 1, 1)

calc_width = 400
calc_height = 550
block_count = 4

screen = pygame.display.set_mode((calc_width, calc_height))


class Button:
    def __init__(self, pos, func):
        self.size = calc_width // block_count
        self.pos = (pos[0] * self.size, pos[1] * self.size + 150)
        self.text = str(func)

        self.surface = pygame.Surface((self.size, self.size))
        self.rect = pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))

    def visualisation(self, pos):       # необходимо визуализировать цифры
        screen.blit(self.surface, self.rect)
        if self.rect.colliderect(pos):
            self.surface.fill((255, 0, 0))
            for num_cell in range(0, 10):
                if self.text == str(num_cell):
                    self.text = num_cell
        else:
            self.surface.fill((255, 255, 255))

        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(str(self.text), True,
                          (180, 0, 0))
        screen.blit(text1, self.rect.center)

        if self.rect.colliderect(pos):
            return self.text


number_one = []

key_massive = [7, 8, 9, "+",
               4, 5, 6, "-",
               1, 2, 3, "*",
               "c", 0, "=", "/"]

buttons = []

for num, i in enumerate(key_massive):
    y = num // block_count
    x = num - (block_count * y)
    buttons.append(Button([x, y], i))

calc_running = True

while calc_running:
    mouse_pos = pygame.Rect(-100, -100, 1, 1)
    keypress_active = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calc_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.Rect(pygame.mouse.get_pos()[0],
                                        pygame.mouse.get_pos()[1],
                                        1,
                                        1)
                keypress_active = True

    for i in buttons:
        new_number = i.visualisation(mouse_pos)
        if new_number in range(0, 10):
            number_one.append(new_number)

    pygame.display.update()
    pygame.time.delay(50)

print(number_one)
