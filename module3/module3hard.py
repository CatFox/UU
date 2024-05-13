def travers(list_, count=0):
    for element in list_:
        if isinstance(element, (list, tuple, set)):
            count = (travers(element, count))
        else:
            if isinstance(element, dict):
                count = travers(element.keys(), count)
                count = travers(element.values(), count)
            else:
                if isinstance(element, (int, float)):
                    count += element
                    print(element, element, count)
                else:
                    if isinstance(element, str):
                        count += len(element)
                        print(element, len(element), count)
    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print("Результат:", travers(data_structure))
