# 2023/10/01 00:00|Домашняя работа по уроку "Функции в Python.Функция с параметром"
# 1) Создайте функцию def print_params, которая в своем теле будет распечатывать переданное значение
# из параметра 2 раза!
# 2) Вызовите данную функцию несколько раз в том же файле
# 3) Запустите поэтапное выполнение программы, нажмите на иконку дебага справа от запуска проекта "жучок"
# 4) В консоли посмотрите на результат программы
# 5) Используйте Step Over (см. скриншот) для перехода к следующему шагу выполнения программы
# 6) Посмотрите на консоль и на ход выполнения программы

def print_params(value):
    for i in range(2):
        print(value)


for i in range(3):
    print_params("значение")