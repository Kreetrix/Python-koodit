import random


while True:
    random_value: int = random.randint(1, 10)
    try:
        input_value = int(input("Arvaa numero 1...10\n"))
        if 1 <= input_value <= 10:
            if input_value > random_value:
                print(f"Liian suuri arvaus, arpottu kokonaisluku on {random_value}")
            elif input_value < random_value:
                print(f"Liian pieni arvaus, arpottu kokonaisluku on {random_value}")
            elif random_value == input_value:
                print(f"Arvasit oikein!!!!")
                break
    except ValueError as err:
        print(f"Error message!!!!!! -> {err.args}")
