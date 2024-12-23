from Furniture import Furniture, MagicKettle
from Room import Room

# Создание мебели
bed = Furniture("Кровать", "Вы ложитесь и немного отдыхаете.", effects={"mood": 20, "health": 10})
table = Furniture("Стол", "Вы садитесь за стол и начинаете учиться.", effects={"study": 10, "mood": -5})
magic_kettle = MagicKettle(
    "Магический чайник",
    "Вы наливаете чай, и чайник начинает шептать что-то магическое."
)

# Создание комнат с мебелью
room_dorm = Room("Комната в общаге", "Небольшая, но уютная комната с кроватью и столом.", furniture=[bed, table, magic_kettle])
room_corridor = Room("Коридор", "Длинный коридор общежития, пахнет странно.")

# Список комнат
rooms = {
    "dorm": room_dorm,
    "corridor": room_corridor
}