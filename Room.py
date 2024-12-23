class Room:
    def __init__(self, roomName, descr, doors=None, furniture=None):
        self.name = roomName
        self.descr = descr
        self.doors = doors if doors else []
        self.furniture = furniture if furniture else []

    def describe(self):
        print(f"Вы находитесь в: {self.name}")
        print(self.descr)
        if self.doors:
            print("Двери ведут в:")
            for door in self.doors:
                print(f"- {door.name}")
        if self.furniture:
            print("Мебель в комнате:")
            for item in self.furniture:
                print(f"- {item.name}")