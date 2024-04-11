import random

n = 0  # Amount of dots that hit the circle
while True:
    try:
        N = int(input("Syötä pisteiden määrä: "))  # Amount of dots
        for i in range(N):
            y = random.uniform(-1, 1)
            x = random.uniform(-1, 1)
            if (x ** 2 + y ** 2) < 1:
                n += 1

        pi = 4 * n / N
        print(f"Pi:in likiarvo -> {pi}")

    except ValueError as err:
        print(f"Error -> {err.args}")
