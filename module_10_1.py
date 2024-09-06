import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


if __name__ == '__main__':
    start_time = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    end_time = time.time()
    duration = end_time - start_time
    print("Работа потоков:", duration)
    start_time_2 = time.time()
    res1 = Thread(target=write_words, args=(10, 'example5.txt'))
    res2 = Thread(target=write_words, args=(30, 'example6.txt'))
    res3 = Thread(target=write_words, args=(200, 'example7.txt'))
    res4 = Thread(target=write_words, args=(100, 'example8.txt'))
    res1.start()
    res2.start()
    res3.start()
    res4.start()

    res1.join()
    res2.join()
    res3.join()
    res4.join()

    end_time_2 = time.time()
    duration_2 = end_time_2 - start_time_2
    print("Работа потоков:", duration_2)
