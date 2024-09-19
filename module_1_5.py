immutable_var = (1, 2, True, 'string', 1.5, [3, 4])
print('Неизменяемый кортеж - ', immutable_var)
# immutable_var[1] = 10 , операциия невозможна, так как кортеж, является неизменяемой коллекцией, которая может содержать изменяемые типы
mutable_list = [1, 2, True, 'str']
print('Изменяемый список - ', mutable_list)
mutable_list[2] = 3
print('Измененный список -', mutable_list)