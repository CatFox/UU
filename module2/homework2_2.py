# # 2023/09/30 00:00|Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
# 1) Создайте список из 5 машин - ["BMW", "MB", "LADA", "KIA", "HONDA"]
# 2) Создайте цикл for и в цикле распечатайте каждый из автомобилей в строке 'Я езжу на автомабиле марки'
# 3) Создайте целочисленную переменную cars_count = 0
# 4) Напишите в цикле из шага номер 2 увеличение переменной на 10 в каждом шаге цикла (cars_count += 10)
# 5) Посмотрите на консоль и на ход выполнения программы

cars_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
step = 0
cars_count = 0
for car in cars_list:
    step += 1
    print("Я езжу на автомабиле марки:", car)
    if step >= 2:
        cars_count += 10
print(cars_count)

