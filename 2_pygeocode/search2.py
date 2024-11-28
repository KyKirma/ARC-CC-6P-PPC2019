import requests

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()

    for x, item in enumerate(reply, start=1):
        cep = item["display_name"].split(',')[-2]

        print(f"    Resultado {x}:")
        print(f"        CEP: {cep}")
        print(f"        (Latitude, Longitude): ({item['lat']}, {item['lon']})")


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')