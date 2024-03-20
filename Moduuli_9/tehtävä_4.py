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


auto = Auto("ABC-123", 142)
contestants = []
for i in range(1, 11):
    print(i)
    contestants.append(Auto(f"ABC-{i}", random.randint(100, 200)))

game = True
while game:
    for x in contestants:
        x.accelerate(random.randint(-10, 15))
        x.I_drive(1)
        if x.distance_traveled >= 10000:
            game = False

for x in contestants:
    print(f"------------------------------------------")
    print(f"Car number -> {x.reg_num}")
    print(f"Max speed -> {x.max_speed}")
    print(f"Distance traveled -> {x.distance_traveled}")
    print(f"------------------------------------------\n")



