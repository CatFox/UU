x = 38
print("Дратути!")
if x < 0 :
    print("меньше нуля.")
print("дотвидания!")

# примеры

a, b = 10, 5
if a > b:
    print("a > b")
if a > b and a > 0:
    print("a > b and a > 0: успех")
if (a > b) and (a > 0 or b < 1000):
    print("(a > b) and (a > 0 or b < 1000): успех")
if 5 < b and b < 10:
    print("5 < b and b < 10: успех")

# сравнение строк и других типов данных

if "34" > "123":
    print('"34" > "123": успех')
if "123" > "12":
    print('"123" > "12": успех"')
if [1, 2] > [1, 1]:
    print("[1, 2] > [1, 1]: успех")

# нельзя сравнивать разные типы
# if "6" > 5:
#    print("успех")
# if [5, 6] < 5:
#    print("успех")
if "6" != 5:
    print('"6" != 5: успех')