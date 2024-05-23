# 2* Усложненный вариант:
# Дан несортированный список, заполненный случайными положительными числами,
# выводить корни тех элементов, которые больше среднего арифметического чисел кратных 5.
# Список должен состоять из 10 000 элементов, поэтому придумать оптимизацию,
# чтобы не проходить весь список, если возможно.
import random


def make_list():
    list_ = []
    for i in range(1, 10001):
        list_.append(random.randint(1, 10000))
    return list_


main_list = make_list()
average = sum(main_list) / len(main_list)
print("Среднее арифметическое:", average)
main_list.sort(reverse=True)
for number in main_list:
    if number > average:
        if number % 5 == 0:
            print(number ** 0.5)
    else:
        break
