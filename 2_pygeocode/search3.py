import http.client
import json
from urllib.parse import quote_plus

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    
    for x, item in enumerate(reply, start=1):
        cep = item["display_name"].split(',')[-2]

        print(f"    Resultado {x}:")
        print(f"        CEP: {cep}")
        print(f"        (Latitude, Longitude): ({item['lat']}, {item['lon']})")


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')