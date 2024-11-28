from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one = False)
    print(location)
    print(f"Endereço Buscado: {address}")
    for x, item in enumerate(location, start=1):
        result = item.raw
        cep = result["display_name"].split(',')[-2]

        print(f"    Resultado {x}:")
        print(f"        CEP: {cep}")
        print(f"        (Latitude, Longitude): ({item.latitude},{item.longitude})")
