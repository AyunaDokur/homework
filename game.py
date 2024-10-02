
def draw_area():
    for i in area:
        print(*i)
    print()
def check_winner():
    print()
area = [['*','*','*'], ['*','*','*'], ['*','*','*']]
print('Welcome!')
print('--------------------')
draw_area()
for turn in range(1, 10):
    print(f'Turn:{turn}')
    if turn % 2 == 0:
        turn_char ='0'
        print('Turn of 0')
    else:
        turn_char = 'X'
        print('Turn of X')
    row = int(input('Choose row 1, 2, 3: ')) - 1
    column = int(input('Choose column 1, 2, 3: ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Area is occupied, you lose your turn!')
        draw_area()
        continue
    draw_area()

