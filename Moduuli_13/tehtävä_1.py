from flask import Flask, Response
import json

app = Flask(__name__)


def prime_number_calc(value: int) -> bool:
    step_1 = value % (1 and value) == 0
    for i in range(2, value):
        if value != i and value % i == 0:
            return False
    if step_1:
        return True


@app.route('/alkuluku/<number>')
def main(number):
    try:
        prime = prime_number_calc(int(number))

        status = 200
        res = {
            "Number": number,
            "isPrime": prime
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
