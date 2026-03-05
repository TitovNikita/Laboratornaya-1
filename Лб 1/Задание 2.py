players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle = len(players) // 2  # индекс середины
first_team = players[:middle]  # первая команда
second_team = players[middle:]  # вторая команда
print(first_team)
print(second_team)
