def custom_write(file_name, string):
    number_of_string = 0
    strings_positions = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    for line in string:
        number_of_string += 1
        number_of_byte = file.tell()
        strings_positions[(number_of_string, number_of_byte)] = line
        file.write(f'{line}\n')
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