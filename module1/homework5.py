my_list = ["яблоко", "ананас", "дыня", "киви", "апельсин", "слива"]
print(my_list)
print("Первый элемент списка -", my_list[0], ", а последний -", my_list[-1], ".")
print("Элементы списка с третьего по пятый: ", my_list[2:5])
my_list[2] = "банан"
print("Элементы после изменения третьего элемента:", my_list)

my_dict = {"apple":"яблоко", "pineapple": "ананас", "melon": "дыня", "kiwi": "киви", "orange": "апельсин", "plum": "слива"}
print("Словарь:", my_dict)
print("Перевод слова 'pineapple' на русский -", my_dict["pineapple"])
my_dict["banana"] = "банан"
print("Измененный словарь:", my_dict)