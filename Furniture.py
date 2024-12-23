import random

# Базовый класс мебели
class Furniture:
    def __init__(self, name, action, effects=None):
        self.name = name
        self.action = action
        self.effects = effects if effects else {}

    def interact(self, player):
        print(f"Вы взаимодействуете с {self.name}: {self.action}")

        for attr, change in self.effects.items():
            current_value = getattr(player, attr, None)
            if current_value is not None:
                new_value = max(0, min(current_value + change, 100))
                setattr(player, attr, new_value)

        self.custom_action(player)
        print("Ваши характеристики обновлены!")

    def custom_action(self, player):
        pass


# Дочерний класс для Магического чайника
class MagicKettle(Furniture):
    def __init__(self, name, action):
        super().__init__(name, action)

    def custom_action(self, player):
        jokes = [
            "Колобок повесился",
            "Тортик это ложь",
            "Совет от чайника: Пей больше воды!"
        ]
        print("\nЧайник начинает говорить...")
        print(random.choice(jokes))