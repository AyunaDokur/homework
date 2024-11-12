
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = bool):
        self.title =title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = None

