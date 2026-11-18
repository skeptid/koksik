# Класс для хранения информации о стримере
class Streamer:
    def __init__(self, nick, followers):
        self.nick = nick
        self.donates = []  # список сумм донатов
        self.followers = followers

    # Добавление доната
    def add_donate(self, amount):
        self.donates.append(amount)

    # Подсчёт общей суммы донатов
    def total_donates(self):
        return sum(self.donates)

    # Подсчёт среднего доната
    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return sum(self.donates) / len(self.donates)


# Функция вывода статистики
def print_stats(streamer):
    print("=== Статистика стримера ===")
    print("Ник:", streamer.nick)
    print("Подписчики:", streamer.followers)
    print("Всего донатов:", streamer.total_donates())
    print("Средний донат:", streamer.average_donate())


# Создание объекта
streamer = Streamer("GolubKin", 1200)
streamer.add_donate(500)
streamer.add_donate(150)

# Вывод статистики
print_stats(streamer)
print("проверка запуска")