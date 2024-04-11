from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metroRoot',
    autocommit=True
)


class Distance:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


def fetch_one(document: str):
    try:
        cursor = connection.cursor()
        cursor.execute(document)
        result = cursor.fetchone()
        if cursor.rowcount > 0:
            return result
        return None

    except mysql.connector as err:
        print(err)


def calculate_distance(ICAO_1: str, ICAO_2: str):
    result_1 = fetch_one(f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport where ident='{ICAO_1}'")
    if result_1 is not None:
        formatted_result = {'latitude_deg': result_1[0], 'longitude_deg': result_1[1]}
        distance_1 = Distance
        distance_1.latitude = formatted_result['latitude_deg']
        distance_1.longitude = formatted_result['longitude_deg']
        airport_1 = (distance_1.latitude, distance_1.longitude)
    else:
        return "First airport ICAO code not found"

    result_2 = fetch_one(f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport where ident='{ICAO_2}'")
    if result_2 is not None:
        formatted_result = {'latitude_deg': result_2[0], 'longitude_deg': result_2[1]}
        distance_2 = Distance
        distance_2.latitude = formatted_result['latitude_deg']
        distance_2.longitude = formatted_result['longitude_deg']
        airport_2 = (distance_2.latitude, distance_2.longitude)
    else:
        return "Second airport ICAO code not found"

    return distance.distance(airport_1, airport_2).km


while True:
    airport = input('Do you want to find an Airport? (y/n): ').lower().strip() == 'y'
    if airport:
        ICAO_1 = input('Input first airport ICAO code -> ')
        ICAO_2 = input('Input second airport ICAO code -> ')
        result = calculate_distance(ICAO_1, ICAO_2)
        if result is not None:
            print(f"Airport -> {result}")
        else:
            print(f"Not found!")
        continue
    airport_insert = input('Do you want to exit? (y/n): ').lower().strip() == 'y'
    if airport_insert:
        print(f"Kicking out!")
        break
