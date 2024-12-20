from random import choice

# lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda first_str, second_str: first_str == second_str, first, second)))

# замыкание

def get_advanced_writer(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        pass

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for line in data_set:
                file.write(str(line) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# methode CALL
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Yes', 'No', 'Maybe')
print(first_ball())
print(first_ball())
print(first_ball())




