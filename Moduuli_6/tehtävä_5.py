import random


def get_rid_of_em(number_list: []) -> [int]:
    purified_list: [int] = []
    for i in range(0, len(number_list)):
        if number_list[i] % 2 == 0:
            purified_list.append(number_list[i])
    return purified_list


while True:
    input("Press enter to generate and sum even numbers")
    origin_list: [int] = []
    for i in range(0, 10):
        origin_list.append(random.randint(1, 100))
    print(f"Origin list -> {origin_list}")
    print(f"Purified list -> {get_rid_of_em(origin_list)}")
