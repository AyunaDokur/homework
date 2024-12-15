import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        count_of_days = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            enemies = enemies - self.power
            count_of_days += 1
            print(f'{self.name} сражается {count_of_days} день ..., осталось {enemies} воинов \n')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {count_of_days} дней! ')




first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')