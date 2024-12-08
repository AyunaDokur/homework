import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № <номер слова по порядку { str(i+1)} \n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

func_time1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

func_time2 = datetime.now()
print('FUNC WORK TIME', func_time2 - func_time1)

first_time = datetime.now()
thread1 = threading.Thread(target = write_words(10, 'example5.txt'))
thread2 = threading.Thread(target = write_words(30, 'example6.txt'))
thread3 = threading.Thread(target = write_words(200, 'example7.txt'))
thread4 = threading.Thread(target = write_words(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
second_time = datetime.now()

print('THREAD WORK TIME', second_time-first_time)

