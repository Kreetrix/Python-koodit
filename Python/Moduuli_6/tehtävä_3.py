def gallons_to_liters(gallons: float) -> float:
    liters = gallons * 3.785
    return round(liters, 2)


while True:
    try:
        gallon_input = float(input("Syötä gallonamäärän: "))
        if gallon_input >= 0:
            print(f"Syötetty gallonamäärä litroina -> {gallons_to_liters(gallon_input)}")
        else:
            break

    except ValueError as err:
        print(f"Error -> {err.args}")
