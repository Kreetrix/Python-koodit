city_placeholder: [str] = []

print("Syötä viisi kaupunkia: ")
for i in range(1, 6):
    try:
        city_input = str(input(f"Kaupunki {i} -> "))
        city_placeholder.append(city_input)
    except ValueError as err:
        print(f"Error -> {err.args}")


print("Syötetyt kaupungit ->")
for i in range(0, len(city_placeholder)):
    try:
        print(city_placeholder[i])
    except IndexError as err:
        print(f"Error -> {err.args}")
