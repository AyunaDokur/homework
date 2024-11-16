team1_num = int(input('Введите количестко участников 1 команды: '))
team2_num = int(input('Введите количестко участников 1 команды: '))
score_1 = int(input('Введите количестко задач решенных 1 командой: '))
score_2 = int(input('Введите количестко задач решенных 2 командой: '))
team1_time = float(input('Введите время потраченное 1 командой: '))
team2_time =  float(input('Введите время потраченное 2 командой: '))
tasks_total = score_2 + score_1
time_avg = round((team2_time + team1_time) / tasks_total, 1)

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных'
else:
    challenge_result = 'Ничья!'



print("\nВ команде Мастера кода участников: %(team1_num)s!" % {'team1_num' : team1_num})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num' : team1_num, 'team2_num' : team2_num})

print("\nКоманда Волшебники данных решила задач: {score_2}!".format(score_2 = score_2))
print("Волшебники данных решили задачи за {team1_time} с !".format(team1_time = team1_time))

print(f'\nКоманды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')