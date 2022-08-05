'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах'''

def read_from_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def write_to_file(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)

def encode(text):
    #with_ones = list(zip(text, [1] * len(text))
    result_tuples = []
    
    count = 1
    for i, c in enumerate(text):
        if i == 0:
            continue
        
        if text[i] == text[i - 1] and count < 9:
            count += 1
        else:
            result_tuples.append((text[i - 1], count))
            count = 1
    
    result_tuples.append((text[-1:], count))
    
    return ''.join([f'{t[1]}{t[0]}' for t in result_tuples])


def decode(text):
    counts = [ int(text[i]) for i, c in enumerate(text) if i % 2 == 0 ]
    chars = [ text[i] for i, c in enumerate(text) if i % 2 != 0 ]
    items = list(zip(counts, chars))
    return ''.join([ count * char for count, char in items])


text = read_from_file('in.txt')
encoded = encode(text)
decoded = decode(encoded)

write_to_file('encoded.txt', encoded)
write_to_file('decoded.txt', decoded)

print(encoded)
print(decoded)


