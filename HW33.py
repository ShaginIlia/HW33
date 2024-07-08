import threading
from time import sleep
import threading as th
import time

c = 1
lock = threading.Lock()
start1 = time.time()
def write_words(word_count, file_name):
    global c
    with open(file_name, 'a', encoding='UTF-8') as file:
        for i in range(word_count):
            with lock:
                file.write('')
                file.write(f'Какое-то слово № {c}' '\n')
                c += 1
                sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


write_words(word_count=10, file_name='exemple1.txt')
write_words(word_count=30, file_name='exemple1.txt')
write_words(word_count=200, file_name='exemple1.txt')
write_words(word_count=100, file_name='exemple1.txt')

end1 = time.time()
res_time1 = end1 - start1
print(res_time1)

start2 = time.time()

one = th.Thread(target=write_words, args=(10, 'exemple2.txt'))
two = th.Thread(target=write_words, args=(30, 'exemple2.txt'))
three = th.Thread(target=write_words, args=(200, 'exemple2.txt'))
four = th.Thread(target=write_words, args=(100, 'exemple2.txt'))

one.start()
two.start()
three.start()
four.start()

one.join()
two.join()
three.join()
four.join()

end2 = time.time()
res_time2 = end2 - start2
print(res_time2)
