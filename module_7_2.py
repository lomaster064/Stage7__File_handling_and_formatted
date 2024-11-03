def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings_positions = {}

    file = open(file_name, 'a', encoding='utf-8')

    for i in range(1, len(strings) + 1):
        pos = file.tell()
        key = (i, pos)
        value = strings[i - 1]

        strings_positions[key] = value

        file.write(value + '\n')

    file.close()

    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)