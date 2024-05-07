import random

stone1 = random.randrange(3, 20)
# print(stone1)
stone2 = ""
list_comb_numbers = []
for i in range(1, 21):
    for j in range(1, 21):
        if i != j:
            comb_numbers = [i, j]
            comb_numbers.sort()
            if comb_numbers not in list_comb_numbers:
                list_comb_numbers.append(comb_numbers)
for comb_numbers in list_comb_numbers:
    if stone1 % sum(comb_numbers) == 0:
        # print(comb_number)
        stone2 += f"{comb_numbers[0]}{comb_numbers[1]}"
print(f"На первом камне выпало: {stone1}. Пароль для второго камня: {stone2}")
