import random


def summer(num_list: [int]) -> int:
    return sum(num_list)


while True:
    input("Press enter to generate and sum even numbers")
    even_numbers: [int | None] = []
    for i in range(0, 10):
        even_numbers.append(random.randint(1, 100) * 2)
    print(summer(even_numbers))
