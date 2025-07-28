# Bots AFK Minecraft

Ce projet permet de lancer des bots AFK (away-from-keyboard) sur un serveur Minecraft.  
Les bots se connectent au serveur et restent inactifs, simulant ainsi une présence automatique.

---

## Fonctionnalités

- Connexion simple à un serveur Minecraft en mode **offline** (sans authentification Mojang).
- Scripts pour lancer plusieurs bots simultanément sous Windows et Linux/macOS.
- Facile à utiliser et à personnaliser.

---

## Prérequis

- Python 3.x installé
- Module Python `minecraft` (pyCraft) installé :

```bash
pip install minecraft
````

* Pour Windows : invite de commandes (.bat)
* Pour Linux/macOS : terminal (.sh)

---

## Usage

### 1. Script Python — `bot_afk.py`

Ce script lance un bot Minecraft qui se connecte au serveur et reste AFK.

```python
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
```

---

### 2. Lancer plusieurs bots sous Windows — `launch_bots.bat`

Ce fichier batch lance plusieurs bots dans des fenêtres de commandes séparées.

```bat
@echo off
REM Lance 3 bots AFK Minecraft sur Windows

start cmd /k python bot_afk.py BotAFK1 play.example.com 25565
start cmd /k python bot_afk.py BotAFK2 play.example.com 25565
start cmd /k python bot_afk.py BotAFK3 play.example.com 25565
```

Pour exécuter :

1. Place `bot_afk.py` et `launch_bots.bat` dans le même dossier.
2. Double-clique sur `launch_bots.bat` ou lance-le dans un terminal.

---

### 3. Lancer plusieurs bots sous Linux/macOS — `launch_bots.sh`

Script shell qui lance plusieurs bots en arrière-plan.

```bash
#!/bin/bash
# Lance 3 bots AFK Minecraft sous Linux/macOS

python3 bot_afk.py BotAFK1 play.example.com 25565 &
python3 bot_afk.py BotAFK2 play.example.com 25565 &
python3 bot_afk.py BotAFK3 play.example.com 25565 &

wait
```

Pour exécuter :

```bash
chmod +x launch_bots.sh
./launch_bots.sh
```

---

## Remarques importantes

* Remplace `play.example.com` par l'adresse de ton serveur Minecraft.
* Ces bots fonctionnent **uniquement** sur les serveurs en mode **offline** (sans authentification Mojang).
* Lancer plusieurs bots peut consommer beaucoup de ressources.
* Utiliser des bots sur des serveurs où cela est interdit peut entraîner un ban.
* Ce projet est à usage éducatif uniquement.

---
