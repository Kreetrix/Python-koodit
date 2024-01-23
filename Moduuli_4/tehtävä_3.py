array_of_numbers: [int] = []
print("Syötä luvut")
while True:
    value: int | str = input("")
    try:
        int(value)
        array_of_numbers.append(value)
    except:
        print(f"Suurin numero: {str(max(array_of_numbers))}")
        print(f"Pienin numero: {str(min(array_of_numbers))}")
        break
