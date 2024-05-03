immutable_var = (2, "flower", True, 41.3)
print("Immutable tuple:", immutable_var)
# immutable_var[0] = 3
# Изменить элементы кортежа нельзя, так как кортеж — это неизменяемый тип данных.
# Для этого предназначен другой тип — списки.
mutable_list = [True, 21, "home", 11.25]
print("Mutable list before changes:", mutable_list)
mutable_list[1] = "1 мая"
print("Mutable list after changes: ", mutable_list)