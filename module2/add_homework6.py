# 6. Напишите функцию convert(L), принимающую на вход список,
# состоящий из чисел и строк вида: [1, 2, '3', '4', '5', 6], и возвращающую список целых чисел (в том же порядке):
# [1, 2, 3, 4, 5, 6]

def convert(L):
    result = []
    for int_ in L:
        result.append(int(int_))
    return result


list_ = [1, 2, '3', '4', '5', 6]

print(convert(list_))
