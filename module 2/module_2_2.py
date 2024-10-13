first = input('Первое число: ')
second = input('Второе число: ')
third = input('Третье число: ')
if len(first) == 0 or len(second)== 0 or len(third) == 0:
    print('Найдено пустое занчение, повторите попытку!')
else:
    if first == second == third:
        print('Найдено 3 совпадения')
    elif first == second or first == third or second == third:
        print('Найдено 2 совпадения')
    else:
        print('Найдено 0 совпадений')
