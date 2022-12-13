# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_encode.txt', 'w') as data:
    data.write('aaaaaaaaaaaAAAAAAbbbb')
with open('file_encode.txt', 'r') as data:
    my_str = data.readline()
print('Обычный текст: ' + my_str)


def encode(txt):
    res = ""
    i = 0
    while i < len(txt):
        count = 1
        while i + 1 < len(txt) and txt[i] == txt[i + 1]:
            count += 1
            i += 1
        res += str(count) + txt[i]
        i += 1
    return res


def decode(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


encoded = encode(my_str)

with open('file_encode.txt', 'r') as file:
    decoded = file.read()
with open('file_decode.txt', 'w') as file:
    encoded = encode(decoded)
    file.write(encoded)

print('Сжатый текст: ' + encoded)

print('Восстановленный текст: ' + decode(encoded))
