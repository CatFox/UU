def travers(list_, count=0):
    for element in list_:
        if isinstance(element, (list, tuple, set)):
            count = (travers(element, count))
        elif isinstance(element, dict):
            count = travers(element.keys(), count)
            count = travers(element.values(), count)
        elif isinstance(element, (int, float)):
            count += element
        elif isinstance(element, str):
            count += len(element)
    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print("Результат:", travers(data_structure))
