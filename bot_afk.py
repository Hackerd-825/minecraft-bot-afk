from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound

def start_bot(username, host, port):
    connection = Connection(host, port, username=username)

    def handle_disconnect(packet):
        print(f"{username} déconnecté du serveur.")

    connection.register_packet_listener(handle_disconnect, clientbound.disconnect_packet)

    connection.connect()
    print(f"{username} connecté au serveur {host}:{port}")

    try:
        while True:
            pass  # Le bot reste AFK, ne fait rien
    except KeyboardInterrupt:
        connection.disconnect()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage : python bot_afk.py <username> <host> <port>")
        sys.exit(1)

    username = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])

    start_bot(username, host, port)
