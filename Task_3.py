'''Создайте два списка — один с названиями языков программирования,
 другой — с числами от 1 до длины первого.
['python', 'c#']
[1,2]
Вам нужно сделать две функции: первая из которых создаст список кортежей,
 состоящих из номера и языка, написанного большими буквами.
[(1,'PYTHON'), (2,'C#')]
Вторая — которая отфильтрует этот список следующим образом: 
если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
то кортеж остается, его номер заменяется на сумму очков.
[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
[(1,'PYTHON'), (102,'C#')]
Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком'''




list_langs = ['python', 'c#', 'java', 'go']
list_numbers = [1, 2, 3, 4]

def word_score(word):
    return sum(map(ord, word))

def divisors(num):
    return [ x for x in range(2, num) if num % x == 0 ]

def create_tuples(list_langs, list_numbers):
    return list(zip(map(str.upper, list_langs), list_numbers))

def filter_list(tuples):
    with_scores = [ (lang, num, word_score(lang)) for lang, num in tuples]
    with_divisors = [ (lang, num, score, divisors(score)) for lang, num, score in with_scores  ]

    return [ (lang, num, score) for lang, num, score, divisors in with_divisors if num not in divisors ]

tuples = create_tuples(list_langs, list_numbers)
print(filter_list(tuples))