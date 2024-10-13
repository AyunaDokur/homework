
n = int(input('input n:'))
list_res = []
sum_of_pair = 0
for i in range(1,n):
    for j in range(2,n):
        sum_of_pair = j + i
        res = n%sum_of_pair
        if res == 0:
            if j == i:
                continue
            if j < i:
                cv = str(j)+str(i)
                flag = True
                for k in list_res:
                    if k == cv:
                        flag =False
                        break
                if flag is True:
                    list_res.append(str(i) + str(j))
            else:
                list_res.append(str(i)+str(j))
#print(*list_res)
result_list = int(''.join(list_res))
print(result_list)
answer_list = [12, 13, 1423, 121524, 162534, 13172635, 1218273645, 141923283746, 11029384756,
               12131511124210394857, 112211310495867, 1611325212343114105968, 1214114232133124115106978,
               1317115262143531341251161079, 11621531441351261171089, 12151811724272163631545414513612711810,
               118217316415514613712811910, 13141911923282183731746416515614713812911]
if result_list in answer_list:
    print('Пароль введен верно!')
else:
    print('Ошибка, пароль не верен')