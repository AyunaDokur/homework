counter = 0

def calculate_structure_sum(*args):
    global counter
    args = list(*args)
    for i in args:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            calculate_structure_sum(i)
        if isinstance(i, dict):
            for j in i:
                counter += len(j)
                if isinstance(i[j], int):
                    counter += i[j]
                else:
                    calculate_structure_sum(i[j])
        if isinstance(i, str):
            counter += len(i)
        if isinstance(i, int):
            counter += i
    return counter

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)