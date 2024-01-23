

while True:
    try:
        input_value = int(input("Syötä kokonaisluku -> "))

        #test = lambda i, a: (i % i == 0)
        #print(test(10))
        x = 21 / 4
        print(x)

        if input_value % (1 and input_value) == 0:
            print("Luku on alkuluku")
        else:
            print("Luku ei ole alkuluku")

    except ValueError as err:
        print(f"Error -> {err.args}")
