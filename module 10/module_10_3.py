import time
import random
import threading

lock = threading.Lock()

class Bank:

    def __init__(self,balance = 0):
        self.balance = balance


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and lock.locked():
                lock.release()
            sum_of_money = random.randint(50, 500)
            self.balance += sum_of_money
            print(f'Пополнение: {sum_of_money} . Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            sum_of_money = random.randint(50, 500)
            print(f'Запрос на {sum_of_money}')
            if sum_of_money <= self.balance:
                self.balance -= sum_of_money
                print(f'Снятие: {sum_of_money}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств!')
                lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')