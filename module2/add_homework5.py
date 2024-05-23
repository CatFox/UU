# 5. Реализуйте в отдельной функции алгоритм Евклида (алгоритм нахождения
# наибольшего общего делителя (НОД) пары целых чисел), возвращая НОД.
# Проверить полученную функцию на списке, состоящем из 10 пар чисел
# (пример пар: [[5, 7], [21, 111], [63, 49]]).

import random


def random_pair_number():
    list = []
    for i in range(10):
        list.append([random.randint(1, 100), random.randint(1, 100)])
    return list


list_pair_number = random_pair_number()

for pair_number in list_pair_number:
    max_number = max(pair_number)
    while max_number != 0:
        if pair_number[0] % max_number == 0 and pair_number[1] % max_number == 0:
            NOD = max_number
            break
        else:
            NOD = "Не найден"
            max_number -= 1
    print(pair_number, "Наибольший общий делитель пары", NOD)
