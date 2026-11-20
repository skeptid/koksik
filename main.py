# Класс стримера
class Streamer:
    def __init__(self, nick, followers):
        self.nick = nick
        self.donates = []      # список сумм донатов
        self.followers = followers

    # добавляет донат в список
    def add_donate(self, amount):
        self.donates.append(amount)

    # сумма всех донатов
    def total_donates(self):
        total = 0
        for d in self.donates:
            total += d
        return total

    # средний донат; если список пуст — 0
    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)


# функция вне класса: печатает статистику
def print_stats(streamer):
    print("=== Статистика стримера ===")
    print("Ник:", streamer.nick)
    print("Подписчики:", streamer.followers)
    print("Всего донатов:", streamer.total_donates())
    print("Средний донат:", streamer.average_donate())


# главная часть
streamer = Streamer("GolubKin", 1200)
streamer.add_donate(500)
streamer.add_donate(150)
print_stats(streamer)