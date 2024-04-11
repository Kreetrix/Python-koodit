sex_male: {str} = {'male', 'm'}
male_hemoglobin: {int} = [117, 175]
sex_female: {str} = {'female', 'f'}
female_hemoglobin: [int] = [134, 195]


def hemoglobin_calc(hemoglobin: male_hemoglobin):
    hemoglobin_value = int(input("Sötä hemoglobiiniarvosi: \n"))
    if hemoglobin[0] >= hemoglobin_value:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemoglobin[1] <= hemoglobin_value:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on kunnossa")


while True:
    try:
        sex_input = str(input("Syötä sukupuolisi: \n")).casefold()
        if sex_input in sex_male:
            hemoglobin_calc(male_hemoglobin)
            break
        elif sex_input in sex_female:
            hemoglobin_calc(female_hemoglobin)
            break

    except ValueError as err:
        print(f"Error -> {err.args}")
