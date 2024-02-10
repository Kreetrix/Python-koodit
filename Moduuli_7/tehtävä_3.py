import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metroRoot',
    autocommit=True
)


def find_airport(ICAO: str):
    document = f"SELECT name FROM airport where ident='{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(document)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result
    return None


def update_airport(ICAO: str, name: str):
    document = f"UPDATE airport SET name='{name}' where ident='{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(document)
    if cursor.rowcount == 1:
        print("Data successfully updated!")
    else:
        print("Database error")


while True:
    airport = input('Do you want to find an Airport? (y/n): ').lower().strip() == 'y'
    if airport:
        airport_ICAO = input('Input airport ICAO code -> ')
        result = find_airport(airport_ICAO)
        if result is not None:
            print(f"Airport -> {result}")
        else:
            print(f"Not found!")
        continue
    airport_insert = input('Do you want to insert a new Airport? (y/n): ').lower().strip() == 'y'
    if airport_insert:
        airport_ICAO = input('Input new airport ICAO code -> ')
        airport_name = input('Input new airport name -> ')
        update_airport(airport_ICAO, airport_name)
        continue
    airport_insert = input('Do you want to exit? (y/n): ').lower().strip() == 'y'
    if airport_insert:
        print(f"Kicking out!")
        break
