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


auto = Auto("ABC-123", 142)
auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)
print(auto.current_speed)
auto.accelerate(-200)
print(auto.current_speed)
