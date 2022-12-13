# Создайте программу для игры в ""Крестики-нолики""

board = list(range(1, 10))


def draw_board(b):
    for i in range(3):
        print(b[0 + i * 3],  b[1 + i * 3],  b[2 + i * 3])


def make_move(symbol):
    valid = False
    while not valid:
        move = input("Куда поставим " + symbol + "? ")
        move = int(move)
        if 1 <= move <= 9:
            if str(board[move - 1]) not in "XO":
                board[move - 1] = symbol
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы ходить.")


def check_win(b):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if b[each[0]] == b[each[1]] == b[each[2]]:
            return b[each[0]]
    return False


def main(b):
    counter = 0
    win = False
    while not win:
        draw_board(b)
        if counter % 2 == 0:
            make_move("X")
        else:
            make_move("O")
        counter += 1
        if counter > 4:
            tmp = check_win(b)
            if tmp:
                print(tmp, "выиграл!")
                win = True
        if counter == 9:
            print("Ничья!")
            break
    draw_board(b)


main(board)
