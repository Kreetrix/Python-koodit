class Auto:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 60
        self.distance_traveled = 2000

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
auto.I_drive(1.5)
print(auto.distance_traveled)