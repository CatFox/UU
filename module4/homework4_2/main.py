def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

## inner_function() - нельзя вызвать функцию так как она вне зоны видимости
test_function()