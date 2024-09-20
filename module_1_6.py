my_dict = {'Alex': 1997, 'Moris': 1990, 'Amy': 2003, 'Monika': 1995}
print('Dictionary:',my_dict)
print('Existing value:', my_dict['Moris'])
print('Not existing value:', my_dict.get('Sofia'))
my_dict.update({'Sofia': 2001,
                'Ricky': 2002})
del_pair = my_dict.pop('Alex')
print('Deleted value:', del_pair)
print('Modified dictionary:', my_dict)

print('\t')

my_set = {1, 2, 3, 2, 1, 'String', 'String', (7,8,9)}
print('Исходное множество: ', my_set)
my_set.add(6)
my_set.add('str')
my_set.discard(3)
print('Обновленное множество: ', my_set)