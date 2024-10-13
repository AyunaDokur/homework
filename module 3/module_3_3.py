def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(4)
print_params(5,6)
print_params(7, 8, 9)
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [21, 'str', False]
values_dict = {'a' : 'Not string',
               'b' : 100,
               'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 45.25]
print_params(*values_list_2, 42)