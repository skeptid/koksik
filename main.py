class Streamer:
    def __init__(self, nickname, subscribers):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = []   # список сумм донатов

    def add_donate(self, amount):
        self.donates.append(amount)

    def total_donates(self):
        return sum(self.donates)

    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)


# Создаём объект (эти строки, скорее всего, потерялись)
streamer = Streamer("GolubKin", 1200)
streamer.add_donate(500)
streamer.add_donate(150)

# Новая функция из Задания 7
def print_stats(streamer):
    print(f"Стример: {streamer.nickname}")
    print(f"Подписчики: {streamer.subscribers}")
    print(f"Всего донатов: {streamer.total_donates()}")
    print(f"Средний донат: {streamer.average_donate()}")

# Вызов функции
print_stats(streamer)