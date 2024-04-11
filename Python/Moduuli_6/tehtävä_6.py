import math


def pizza_calc(diameter: float, cost: float) -> float:
    area = math.pi * (diameter / 2) ** 2
    cost_per_square_meter = cost / area
    return round(cost_per_square_meter, 2)


while True:
    print("Input pizza diameter in centimeters and it's price")
    try:
        pizza_diam_1 = float(input("Input first pizza's diameter in centimeters -> "))
        pizza_cost_1 = float(input("Input first pizza's cost -> "))
        pizza_diam_2 = float(input("Input second pizza's diameter in centimeters ->"))
        pizza_cost_2 = float(input("Input second pizza's cost -> "))
        pizza_1 = pizza_calc(pizza_diam_1, pizza_cost_1)
        pizza_2 = pizza_calc(pizza_diam_2, pizza_cost_2)
        if pizza_1 > pizza_2:
            print(f"Best price per square meter = {pizza_1}")
            print("Pizza 1 has the best price per square meter")
        else:
            print(f"Best price per square meter = {pizza_2}")
            print("Pizza 2 has the best price per square meter")
        break

    except ValueError as err:
        print(f"Error -> {err.args}")