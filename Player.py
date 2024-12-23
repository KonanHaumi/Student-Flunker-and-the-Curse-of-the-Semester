class Player:
    def __init__(self, studentName):
        self.name = studentName
        self.health = 100
        self.mood = 50
        self.study = 0
        self.coords = None

    def move(self, room):
        self.coords = room
        print(f"\n{self.name} переместился в: {room.name}")

    def show_stats(self):
        print("---------------------------------")
        print(f"{self.name} - Характеристики:")
        print(f"  Здоровье: {self.health}")
        print(f"  Настроение: {self.mood}")
        print(f"  Учеба: {self.study}")
        print("---------------------------------")

        if self.health == 0:
            print("Ваше здоровье на нуле! Вы потеряли сознание.")
            print("Игра окончена!")
            exit()
        if self.mood == 0:
            print("Ваше настроение на нуле! Вы впали в депрессию.")
            print("Игра окончена!")
            exit()

    def interact_with_furniture(self):
        if not self.coords.furniture:
            print("В этой комнате нет ничего, с чем можно взаимодействовать.")
            return

        print("\nС чем вы хотите взаимодействовать?")
        for i, furniture in enumerate(self.coords.furniture):
            print(f"{i + 1}. {furniture.name}")

        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(self.coords.furniture):
                self.coords.furniture[choice].interact(self)
            else:
                print("Неверный выбор. \n")
        except ValueError:
            print("Введите число, соответствующее номеру предмета. \n")