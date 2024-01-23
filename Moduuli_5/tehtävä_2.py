array_of_numbers: [int] = []

print("Syötä kokonaislukuja")
print("Syöttämällä minkä tahansa paitsi kokonaisluku, ohjelma palauttaa syötetyt numerot suuruusjärjestyksessä")
while True:
    input_values: int | str = input("")
    if input_values.isdigit():
        array_of_numbers.append(int(input_values))

    else:
        if len(array_of_numbers) > 0:
            array_of_numbers.sort(reverse=True)
            print(f"Viisi suurinta numeroa suuruusjärjestyksessä -> ")
            for i in range(0, len(array_of_numbers)):
                if int(i) < 5:
                    print(f"{array_of_numbers[i]}")
        break