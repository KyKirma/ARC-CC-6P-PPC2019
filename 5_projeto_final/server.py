import socket

MAX_PLAYERS = 4
players = {}

def broadcast(message, sock):
    for address in players.keys():
        sock.sendto(message.encode('ascii'), address)

def recvall(sock, length):
    data = b''

    # o laço é verdade enquanto não recebermos
    # todos os bytes esperados.
    # No caso deste programa simples são 16 bytes
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))

    sock.listen(1)
    print('Listening at {}'.format(sock.getsockname()))
    print(f'Aguardando jogadores...\n')

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        jogador = data.decode('ascii')

        print(f'{jogador} conectado com sucesso.'.format(address, jogador)) # Mensagem de confirmação de conexão para servidor
        message = f'{jogador} conectado com sucesso.'.format(address, jogador) # Mensagem de confirmação de conexão para cliente
        sock.sendto(message.encode('ascii'), address)

        # Verifica se o jogador já existe na lista players
        NUMPLAYERSNOW = len(players)
        jogador_existe = False
        for addr, nome in players.items():
            if nome == jogador:
                jogador_existe = True
                # Atualiza o endereço do jogador
                del players[addr]
                players[address] = jogador
                break

        if not jogador_existe:
            players[address] = jogador  # Adiciona o jogador ao dicionário players

        if len(players) == 1:
            player_mestre = list(players.keys())[0]

        message = 'Jogadores na sala:\n'
        for addr, nome in players.items():
            message += f'     {nome}     {addr}\n'
        message += f'\nNumero de jogadores na sala: {len(players)}/{MAX_PLAYERS}\n'

        print(message)
        broadcast(message, sock)

        if NUMPLAYERSNOW != len(players):
            broadcast(message, sock)

if __name__ == '__main__':
    server("", 1060)

    