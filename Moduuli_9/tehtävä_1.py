class Auto:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0


auto = Auto("ABC-123", 142)
print(f"{auto.reg_num}, {auto.max_speed}, {auto.current_speed}, {auto.distance_traveled}")