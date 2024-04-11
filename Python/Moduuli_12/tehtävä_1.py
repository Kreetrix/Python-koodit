import json

import requests

res = requests.get(f'https://api.chucknorris.io/jokes/random')
data = json.loads(res.text)
print(f'Chuck Norris fact -> {data['value']}')