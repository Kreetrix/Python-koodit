import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metroRoot',
    autocommit=True
)


def find_airport(iso_country: str):
    document = f"SELECT airport.name, airport.iso_country, airport.type FROM airport where airport.iso_country='{iso_country}'"
    cursor = connection.cursor()
    cursor.execute(document)
    result = cursor.fetchall()
    formatted_result = [{'name': row[0], 'iso_country': row[1], 'type': row[2]} for row in result]
    if cursor.rowcount > 0:
        return formatted_result
    return None


class Types:
    def __init__(self, heliport: int, small_airport: int, medium_airport: int, large_airport: int):
        self.heliport = heliport
        self.small_airport = small_airport
        self.medium_airport = medium_airport
        self.large_airport = large_airport


while True:
    airport = input('Do you want to find an Airport? (y/n): ').lower().strip() == 'y'
    if airport:
        airport_ICAO = input('Input airport country ISO code -> ').upper()
        result = find_airport(airport_ICAO)
        if result is not None:
            types = Types(0, 0, 0, 0)
            for i in range(len(result)):
                if result[i]['type'] == "heliport":
                    types.heliport += 1
                elif result[i]['type'] == "small_airport":
                    types.small_airport += 1
                elif result[i]['type'] == "medium_airport":
                    types.medium_airport += 1
                elif result[i]['type'] == "large_airport":
                    types.large_airport += 1

            print(f'Heliports -> {types.heliport}')
            print(f'Small airports -> {types.small_airport}')
            print(f'Medium airports -> {types.medium_airport}')
            print(f'Large airports -> {types.large_airport}')
        else:
            print(f"Not found!")
        continue
    airport_insert = input('Do you want to exit? (y/n): ').lower().strip() == 'y'
    if airport_insert:
        print(f"Kicking out!")
        break
