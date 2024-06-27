from nim_engene import get_bunches, put_stones, is_game_over, take_from_bunch

put_stones()

while True:
    print("Текущая позиция")
    print(get_bunches())
    pos = input("От куда берем?")
    qua = input("Сколько берем?")
    take_from_bunch(pos, qua)
    if is_game_over():
        break