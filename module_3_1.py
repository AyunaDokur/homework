
calls = 0

def count_calls():
    return calls

def string_info(string):
    global calls
    calls += 1
    info_tuple = (len(string), string.upper(), string.lower())
    return info_tuple

def is_contains(string, list_):
    global calls
    calls += 1
    string = string.lower()
    for i in range(len(list_)):
        list_[i] = list_[i].lower()
    if string in list_:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)