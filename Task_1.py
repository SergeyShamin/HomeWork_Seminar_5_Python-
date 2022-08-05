'''Напишите программу, удаляющую из текста все слова, содержащие ""абв""'''

from posixpath import split


text = input('Введите текст: ')

print(' '.join(list(filter(lambda word:'абв' not in word, text.split()))))