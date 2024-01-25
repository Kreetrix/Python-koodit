import random

total_rolls = 0


def dice(dice_face_amount: int) -> int:
    return random.randint(1, dice_face_amount)


dice_face_amount = int(input("Syötä nopan tahkojen yhteismäärän: "))
while True:
    dice_roll = dice(dice_face_amount)
    if dice_roll == dice_face_amount:
        print(f"Finally, the largest number -> {dice_face_amount}")
        print(f"Total dice rolls -> {total_rolls}")
        break
    print(f"Rolled -> {dice_roll}")
    total_rolls += 1
