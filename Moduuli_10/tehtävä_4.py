import random


class Auto:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed):
        change = self.current_speed + speed
        if 0 > change:
            self.current_speed = 0
        elif self.max_speed < change:
            self.current_speed = self.max_speed
        else:
            self.current_speed = change

    def I_drive(self, hours):
        self.distance_traveled += self.current_speed * hours

class Kilpailu:
    def __init__(self):
        self.competition_name = "Suuri romuralli"
        self.length = 100
        self.contestants = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    def hour_passes(self):
        for i in range(len(self.contestants)):
            self.contestants[i].accelerate(random.randint(-10, 15))
            self.contestants[i].I_drive(1)

    def print_status(self):
        for i in range(len(self.contestants)):
            print(f"------------------------------------------")
            print(f"Car number -> {self.contestants[i].reg_num}")
            print(f"Max speed -> {self.contestants[i].max_speed}")
            print(f"Distance traveled -> {self.contestants[i].distance_traveled}")
            print(f"------------------------------------------\n")

    def competition_over(self) -> bool:
        for i in range(len(self.contestants)):
            if self.contestants[i].distance_traveled >= 8000:
                return True
        return False


k = Kilpailu()
hour = 0
while True:
    k.hour_passes()
    hour += 1
    if hour % 10 == 0:
        k.print_status()
    if k.competition_over():
        k.print_status()
        break









