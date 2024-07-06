class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password



class user:
    """
    Класс пользователя, содержащий атрибуты
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        self.password = password
        if password == password_confirm:
            self.password = password


if __name__ == "__main__":
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин:")
            password = input("Введите пароль:")
            if login in database.data:
                if password == database.data[login]:
                    print("Вход выполненен", login)
                    break
                else:
                    print("Неверный пароль")
                    break
            else:
                print("Пользователь не найден.")
        if choice == 2:
            user = user(input("Введите логин:"), password := input("Введите пароль:"), password2 := input("Повторите пароль:"))
            if password != password2:
                print("Пароли не совпадают, попробуйте еще раз.")
                continue
            database.add_user(user.username, user.password)
        print(database.data)