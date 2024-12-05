import random
import socket

MAX_BYTES = 65535
MAX_PLAYERS = 3

players = {}

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())
    print(f'Número de jogadores na sala: 0/{MAX_PLAYERS}')
    print(f'Aguardando jogadores...')

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        

        jogador = data.decode('ascii')
        print(f'{jogador} conectado com sucesso.'.format(address, jogador))

        message = 'Jogadores na sala:'.format(len(data))
        sock.sendto(message.encode('ascii'), address)


if __name__ == '__main__':
    # Aqui, "" significa que o servidor está habilitado a receber
    # requisições de qualquer umas das interfaces locais
    server("", 1060)