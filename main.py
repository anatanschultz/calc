enter_num = True
massive_x = []


class Number:
    def __init__(self, massive):
        self.massive = massive
        self.output = 0

    def take_number(self):
        for num, i in enumerate(self.massive):
            number_dec = i * 10 ** (len(self.massive) - num - 1)
            self.output += number_dec
        return self.output


while enter_num:
    input_num = int(input())
    if input_num in range(0, 9):
        massive_x.append(input_num)
    else:
        enter_num = False

x = Number(massive_x)

print(x.take_number())
