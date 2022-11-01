pole = [[' '] * 3 for i in range(3)]
print(pole)

def show ():
    print()
    print('      1 | 2 | 3')
    print('  -------------')
    for i, j in enumerate(pole):
        str_ = f"  {i + 1} | {' | '.join(j)} | "
        print(str_)
        print("  --------------- ")

def greeting():
    print('  Добро пожаловать', '\n', '     в игру', '\n',  'крестики - нолики.')
    print('--------------------')
    print('Формат ввода - x, y')
    print('x - номер строки')
    print('y - номер столбца')

def ask_check():
    while True:
        box = input('Введите координаты: ').split()
        if len(box) != 2:
            print('Введите две координаты через пробел')
            continue

        x, y = box
        if not (x.isdigit()) or not (y.isdigit()):
            print( 'Введите числа!')
            continue


        x, y = int(x), int(y)

        if 1 > x or x > 3 or 1 > y or y > 3:
            print( 'Координаты вне диапазона!')
            continue

        if pole[x-1][y-1] != ' ':
            print( 'Клетка занята!')
            continue

        return x, y

def win_chek():
    win_box = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_box:
        symb = []
        for i in cord:
            symb.append(pole[i[0]][i[1]])
        if symb == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symb == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greeting()
pole = [[' '] * 3 for _ in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask_check()

    if count % 2 == 1:
        pole[x-1][y-1] = 'X'
    else:
        pole[x-1][y-1] = '0'

    if win_chek():
        break

    if count == 9:
        print('Ничья!')
        break










