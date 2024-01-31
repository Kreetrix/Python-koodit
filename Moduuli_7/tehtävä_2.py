name_placeholder: [str] = []

while True:
    name = input("Input name -> ")
    if name == "":
        break
    if name not in name_placeholder:
        name_placeholder.append(name)
        print("New name")
    else:
        print("Already exists")

    print(f"placeholder -> {name_placeholder}")
