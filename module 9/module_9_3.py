first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first_str) - len(second_str) for (first_str, second_str) in zip(first,second) if len(first_str) != len(second_str))
second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)
print(list(first_result))
print(list(second_result))
