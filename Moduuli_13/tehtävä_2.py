from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)



connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metroRoot',
    autocommit=True
)

def find_airport(ICAO: str):
    document = f"SELECT airport.name, airport.municipality FROM airport where ident='{ICAO}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(document)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        return result[0]
    return None

@app.route('/kenttä/<code>')
def main(code):
    try:
        result = find_airport(code)
        status = 200
        res = {
            "ICAO": code,
            "Name": result['name'],
            "Municipality": result['municipality']
        }

    except ValueError:
        status = 400
        res = {
            "status": status,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonres = json.dumps(res)
    return Response(response=jsonres, status=status, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
