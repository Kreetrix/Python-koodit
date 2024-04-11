seasons = ['talvi', 'kevät', 'kesä', 'syksy']


def month_to_season(month: int) -> str:
    season_num = int(month / 3)
    print(season_num)
    if season_num >= 4:
        season_num = 0
    return seasons[season_num]


while True:
    try:
        month_num = int(input("Input month as a number between 1 and 12 -> "))
        if 12 >= month_num > 0:
            season = month_to_season(month_num)
            print(f"Season -> {season}")
            break
        else:
            raise ValueError("Input only numbers between 1 and 12")

    except ValueError as err:
        print(f"Error -> {err.args}")
