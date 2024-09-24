first = input('Первое число: ')
second = input('Второе число: ')
third = input('Третье число: ')
while len(first) == 0 or len(second)== 0 or len(third) == 0:
    if len(first) == 0:
        print('Первое число не введено, повторите ввод!')
        first = input('Повторный ввод: ')
    if len(second) == 0:
        print('Второе число не введено, повторите ввод!')
        second = input('Повторный ввод: ')
    if len(third) == 0:
        print('Третье число не введено, повторите ввод!')
        third = input('Повторный ввод: ')
if first == second == third:
    print('Найдено 3 совпадения')
elif first == second or first == third or second == third:
    print('Найдено 2 совпадения')
else:
    print('Найдено 0 совпадений')
