import random


def dice() -> int:
    return random.randint(1, 6)


while True:
    dice_roll = dice()
    if dice_roll == 6:
        print(f"Finally, number six")
        break
    print(f"Rolled -> {dice_roll}")