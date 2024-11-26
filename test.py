
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    print(len(numbers))
    for i in numbers:
        try:
            result += i
        except:
            incorrect_data += 1
    return result, incorrect_data

print(personal_sum([42, 15, 36, 13]))
print(personal_sum('1, 2, 3'))