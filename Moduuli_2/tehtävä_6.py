import random

three_number_code: [int] = []
four_number_code: [int] = []

for i in range(0, 4):
    if i < 3:
        three_number_code.append(random.randint(0, 9))
    four_number_code.append(random.randint(1, 6))


print("Kolmenumeroinen koodi -> " + str(three_number_code))
print("Neljänumeroinen koodi -> " + str(four_number_code))


