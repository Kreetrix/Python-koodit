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


class Electric(Auto):
    def __init__(self, reg_num, max_speed, battery):
        super().__init__(reg_num, max_speed)
        self.battery = battery


class Gas(Auto):
    def __init__(self, req_num, max_speed, gas):
        super().__init__(req_num, max_speed)
        self.gas = gas


e = Electric("ABC-15", 180, 52.2)
g = Gas("ACD-123", 165, 32.3)

e.accelerate(100)
e.I_drive(3)
g.accelerate(160)
g.I_drive(3)
print('Electric:')
print(f'Distance -> {e.distance_traveled}')
print("----------------------------------")
print('Gas')
print(f'Distance -> {g.distance_traveled}')