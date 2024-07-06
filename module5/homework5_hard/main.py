import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = ""

    def log_in(self, nickname, password):
        for user in self.users:
            if user.username == nickname and user.password == hash(password):
                self.current_user = user.nickname

    def register(self, nickname, password, age):
        for user in self.users:
            if user.username == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = nickname

    def log_out(self):
        self.current_user = ""

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        found_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                found_videos.append(video.title)
        return found_videos

    def watch_video(self, name_video):
        if self.current_user == "":
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if video.title == name_video:
                    if video.adult_mode and self.get_current_user_age() < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for i in range(1, video.duration + 1):
                            video.time_now = i
                            print(video.time_now, end=" ")
                            time.sleep(1)
                        print("Конец видео.")

    def get_current_user_age(self):
        for user in self.users:
            if user.username == self.current_user:
                return user.age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time.time()
        self.adult_mode = adult_mode


class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')