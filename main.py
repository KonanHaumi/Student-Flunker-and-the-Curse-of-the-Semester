from Player import Player
from game_data import rooms

# Начало игры
print("\nВы просыпаетесь и вспоминаете ваше ИМЯ")
name = "Студент-" + input('> ')
player = Player(name)

# Начальная комната
player.move(rooms["dorm"])

# Игровой цикл
while True:
    player.show_stats()
    room = player.coords
    room.describe()

    print("\nЧто вы хотите сделать?")
    print("1. Переместиться в другую комнату")
    print("2. Осмотреть комнату")
    #print("3. Выйти из игры")

    try:
        action = int(input("> "))
        if action == 1:
            print("\nКуда вы хотите пойти?")
            for i, door in enumerate(room.doors):
                print(f"{i + 1}. {door.name}")
            try:
                door_choice = int(input("> ")) - 1
                if 0 <= door_choice < len(room.doors):
                    player.move(room.doors[door_choice])
                else:
                    print("Неверный выбор комнаты. \n")
            except ValueError:
                print("Введите число, соответствующее номеру комнаты. \n")
        elif action == 2:
            player.interact_with_furniture()
        elif action == 3:
            print("Спасибо за игру! До встречи!")
            break
        else:
            print("Неверный выбор действия. \n")
    except ValueError:
        print("Введите число, соответствующее действию. \n")