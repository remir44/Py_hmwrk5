# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# player vs smart? bot
import random
from random import choice, randint

print(
    '"~~Игра с конфетами~~"\n'
    'Играют два игрока делая ход друг после друга.\n'
    'На столе лежат конфеты (например, 2021)\n'
    'За один ход можно забрать не более определенного количества конфет (например, 28)\n'
    'Тот, кому достанется последняя конфета - ПРОИГРАЛ\n'
)

messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'Сколько конфет берем?', 'Берите еще', 'Ваш ход']
max_number_move = 0


def introduce_players():
    player1 = input('Введите имя игрока: ')
    player2 = 'El bot'
    print(f'Очень приятно, сегодня Вы играете с {player2}')
    return [player1, player2]


def sweets_game(players):
    global max_number_move
    total_sweets = int(input('Введите сколько всего у нас конфет: '))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход: '))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_sweets, max_number_move, int(first)]


max_move = max_number_move


def player_vs_bot(sweets, players, msges):
    global max_number_move
    count = sweets[2]

    while sweets[0] > 0:
        if sweets[0] == (max_number_move and max_number_move > sweets[0] > 1):
            move = sweets[0] - 1
            print(f'Противник забирает {move}')

        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Противник забирает {move}')
        else:
            print(f'{players[0]}, {choice(msges)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if move <= sweets[0] <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


players_ = introduce_players()
sweets_ = sweets_game(players_)

winner = player_vs_bot(sweets_, players_, messages)
if not winner:
    print('Ничья.')
else:
    print(
        f'Поздравляю! В этот раз победитель - {winner}! Ему достаются все конфеты!')
