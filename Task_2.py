'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''

import random

def human(current_count, max_to_take, max_per_move):
    return int(input('Введите число конфет: '))

def random_bot(current_count, max_to_take, max_per_move):
    return random.randint(1, max_to_take)

current_count = 2021
max_per_move = 28
player_move = random.choice([0, 1])
players = [human, random_bot]

print('Первый ход делает игрок с номером ', player_move + 1)

while True:
    print('-' * 40)
    print('Конфет на столе: ', current_count)
    print('Ход делает игрок с номером ', player_move + 1)
    
    current_max = min(current_count, max_per_move)
    
    while True:
        count = players[player_move](current_count, current_max, max_per_move)
        if count <= max_per_move:
            break
        else:
            print(f'Введите число меньше {max_per_move + 1} ')

    current_count -= count
    print(f'Игрок {player_move + 1} забирает со стола {count} конфет')
    
    if player_move:
        player_move = 0
    else:
        player_move = 1

    if current_count == 0:
        print('Победил игрок с номером ', player_move + 1)
        break