import random
import os


def print_mines_layout():
    global mine_values
    global n

    print()
    print("\t\t\t\t\t\tСАПЁР\n")

    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)

    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______"
            print(st)

        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")

        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|")

        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')

    print()


def set_mines():
    global numbers
    global mines_no
    global n

    count = 0
    while count < mines_no:

        val = random.randint(0, n * n - 1)

        r = val // n
        col = val % n

        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col] = -1


def set_values():
    global numbers
    global n

    for r in range(n):
        for col in range(n):

            if numbers[r][col] == -1:
                continue

            if r > 0 and numbers[r - 1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if r < n - 1 and numbers[r + 1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if col > 0 and numbers[r][col - 1] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if col < n - 1 and numbers[r][col + 1] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if r > 0 and col > 0 and numbers[r - 1][col - 1] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if r > 0 and col < n - 1 and numbers[r - 1][col + 1] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if r < n - 1 and col > 0 and numbers[r + 1][col - 1] == -1:
                numbers[r][col] = numbers[r][col] + 1

            if r < n - 1 and col < n - 1 and numbers[r + 1][col + 1] == -1:
                numbers[r][col] = numbers[r][col] + 1


def neighbours(r, col):
    global mine_values
    global numbers
    global vis

    if [r, col] not in vis:

        vis.append([r, col])

        if numbers[r][col] == 0:

            mine_values[r][col] = numbers[r][col]

            if r > 0:
                neighbours(r - 1, col)
            if r < n - 1:
                neighbours(r + 1, col)
            if col > 0:
                neighbours(r, col - 1)
            if col < n - 1:
                neighbours(r, col + 1)
            if r > 0 and col > 0:
                neighbours(r - 1, col - 1)
            if r > 0 and col < n - 1:
                neighbours(r - 1, col + 1)
            if r < n - 1 and col > 0:
                neighbours(r + 1, col - 1)
            if r < n - 1 and col < n - 1:
                neighbours(r + 1, col + 1)

        if numbers[r][col] != 0:
            mine_values[r][col] = numbers[r][col]


def clear():
    os.system("clear")


def instructions():
    print("Инструкция:")
    print("1. Введите ряд и колонну, например: \"2 3\"")
    print("2. Чтобы установить флаг, введите F после номера ряда и колонны, например: \"2 3 F\"")


def check_over():
    global mine_values
    global n
    global mines_no

    count = 0

    for r in range(n):
        for col in range(n):

            if mine_values[r][col] != ' ' and mine_values[r][col] != 'F':
                count = count + 1

    if count == n * n - mines_no:
        return True
    else:
        return False


def show_mines():
    global mine_values
    global numbers
    global n

    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'


if __name__ == "__main__":

    n = 8

    mines_no = 8

    numbers = [[0 for y in range(n)] for x in range(n)]

    mine_values = [[' ' for y in range(n)] for x in range(n)]

    flags = []

    set_mines()

    set_values()

    instructions()

    over = False

    while not over:
        print_mines_layout()

        inp = input("Введите ряд и колонну через пробел - ").split()

        if len(inp) == 2:

            try:
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Ошибка при вводе!")
                instructions()
                continue

        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                clear()
                print("Ошибка при вводе!")
                instructions()
                continue

            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("Ошибка при вводе!")
                instructions()
                continue

            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("Ошибка при вводе!")
                instructions()
                continue

            r = val[0] - 1
            col = val[1] - 1

            if [r, col] in flags:
                clear()
                print("Флаг здесь уже установлен!")
                continue

            if mine_values[r][col] != ' ':
                clear()
                print("Клетка уже открыта!")
                continue

            if len(flags) < mines_no:
                clear()
                print("Флаг установлен.")

                flags.append([r, col])

                mine_values[r][col] = 'F'
                continue
            else:
                clear()
                print("Флаги кончились.")
                continue

        else:
            clear()
            print("Ошибка при вводе!")
            instructions()
            continue

        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            clear()
            print("Ошибка при вводе!")
            instructions()
            continue

        r = val[0] - 1
        col = val[1] - 1

        if [r, col] in flags:
            flags.remove([r, col])

        if numbers[r][col] == -1:
            mine_values[r][col] = 'M'
            show_mines()
            print_mines_layout()
            print("Вы взорвались. Игра окончена!")
            over = True
            continue

        elif numbers[r][col] == 0:
            vis = []
            mine_values[r][col] = '0'
            neighbours(r, col)

        else:
            mine_values[r][col] = numbers[r][col]

        if (check_over()):
            show_mines()
            print_mines_layout()
            print("Победа!")
            over = True
            continue
        clear()
