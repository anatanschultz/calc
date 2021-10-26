
class Number:
    def __init__(self, massive):
        self.massive = massive
        self.output = 0

    def take_number(self):
        for num, i in enumerate(self.massive):
            number_decade = i * 10**(len(self.massive)-(num+1))
            self.output += number_decade
        return self.output


def create_massive():       # функция требует изменения на вызов математического действия
    massive = []
    enter_num = True
    while enter_num:
        input_num = int(input())
        if input_num in range(0, 9):
            massive.append(input_num)
        else:
            enter_num = False
    return massive


massive_x = create_massive()
massive_y = create_massive()

x = Number(massive_x)
y = Number(massive_y)

print(x.take_number() + y.take_number())
