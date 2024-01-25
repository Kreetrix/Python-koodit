def prime_number_calc(value: int) -> bool:
    step_1 = value % (1 and value) == 0
    # Luultavasti ei ole kovin optimisoitu vaihtoehto, mutta käytin nyt tätä sympy-kirjaston sijaan
    for i in range(2, value):
        if value != i and value % i == 0:
            return False
    if step_1:
        return True


while True:
    try:
        input_value = int(input("Syötä kokonaisluku -> "))

        if prime_number_calc(input_value):
            print("Luku on alkuluku")
        else:
            print("Luku ei ole alkuluku")

    except ValueError as err:
        print(f"Error -> {err.args}")
