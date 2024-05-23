import random


def make_list():
    list_ = []
    for i in range(50):
        list_.append(random.randint(1, 50))
    return list_

main_list = make_list()
average = sum(main_list) / len(main_list)
sorted_list = sorted(main_list)
average_min_max = (sorted_list[0] + sorted_list[-1]) / 2
i = 0

for number in sorted_list:

    if number % 41 == 0 and number > average_min_max:
        i += 1
print("Количество значений кратных 41 и больше среднеарифметического максимального и минимального значения списка:", i)

