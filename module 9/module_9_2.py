first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_len)  for str_len in first_strings if len(str_len) >= 5]
second_result = [(first_str , second_str) for first_str in first_strings for second_str in second_strings if len(first_str) == len(second_str)]
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)