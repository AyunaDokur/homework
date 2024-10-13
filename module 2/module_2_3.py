my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while my_list[count] >= 0:
    if my_list[count] == 0:
        count+=1
        continue
    if len(my_list) - 1 == count:
        print(count)
        print(my_list[count])
        print('Список закончился')
        break
    else:
        print(my_list[count])
        count+=1

