string_ = "Этот код не *спорчен"
list_ = string_.split(" ")
for word in list_:
    if word[0] != "*":
        print(word)