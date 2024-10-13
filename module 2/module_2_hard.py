import random
list_res = []
def rand_first_number():
    n = random.randint(3, 20)
    return n

def answer_is_correct(n):
    answer_list = [12, 13, 1423, 121524, 162534, 13172635, 1218273645, 141923283746, 11029384756,
                   12131511124210394857, 112211310495867, 1611325212343114105968, 1214114232133124115106978,
                   1317115262143531341251161079, 11621531441351261171089, 12151811724272163631545414513612711810,
                   118217316415514613712811910, 13141911923282183731746416515614713812911]
    if n in answer_list:
        print('Пароль введен верно!')
    else:
        print('Ошибка, пароль не верен!')

def password_result(n):
    for i in range(1, n):
        for j in range(2, n):
            sum_of_pair = j + i
            res = n % sum_of_pair
            if res == 0:
                if j == i:
                    continue
                if j < i:
                    current_value = str(j) + str(i)
                    flag = True
                    for k in list_res:
                        if k == current_value:
                            flag = False
                            break
                    if flag is True:
                        list_res.append(str(i) + str(j))
                else:
                    list_res.append(str(i) + str(j))
    return int(''.join(list_res))

first_number = rand_first_number()
print(first_number)
result_number = password_result(first_number)
print(result_number)
answer_is_correct(result_number)
