def get_multiplied_digits(number):
    if number == 0:
        return 0
    else:
        str_number = str(number)
        str_number = str_number.replace('0', '')
        first = int(str_number[0])
        if len(str_number) > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first

result = get_multiplied_digits(int(input('Введите число: ')))
print(result)