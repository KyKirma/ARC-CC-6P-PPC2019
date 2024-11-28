import socket
import ssl
import json
from urllib.parse import quote_plus

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Search4.py\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
    context = ssl.create_default_context()
    with socket.create_connection(('nominatim.openstreetmap.org', 443)) as sock:
        with context.wrap_socket(sock, server_hostname='nominatim.openstreetmap.org') as ssock:
            request = request_text.format(quote_plus(address))
            ssock.sendall(request.encode('ascii'))
            raw_reply = b''
            while True:
                more = ssock.recv(4096)
                if not more:
                    break
                raw_reply += more
            reply = raw_reply.decode('utf-8')
            # Separar cabeçalho do corpo da resposta
            header, body = reply.split('\r\n\r\n', 1)
            
            # Processar o JSON
            items = json.loads(body)
            for x, item in enumerate(items, start=1):
                cep = item["display_name"].split(',')[-2].strip()
                print(f"    Resultado {x}:")
                print(f"        CEP: {cep}")
                print(f"        (Latitude, Longitude): ({item['lat']}, {item['lon']})")

if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')