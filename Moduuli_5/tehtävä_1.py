import random

while True:
    try:
        result = 0
        dice_amount = int(input("Syötä arpakuutioden lukumäärä: "))
        for i in range(dice_amount):
            result += random.randint(1,6)
        print(result)
    except ValueError as err:
        print(f"Error -> {err.args}")