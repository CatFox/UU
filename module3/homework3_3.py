# 1. Создайте новую функцию def test... с произвольным числом параметров разного типа,
#    функция должна распечатывать эти параметры внутри своего тела

def test(n, *args, name="Stanislav", **dict):
    print(n, args, name, dict)


test(1, 1, 2, 3, 4, 5, old="24,", new=41)


# 2. Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре

def factorial(n):
    if n > 0:
        result = n * factorial(n - 1)
    else:
        result = 1
    return result


factorial_n = factorial(int(input("Введите число для вычисления факториала:")))
print(factorial_n)


