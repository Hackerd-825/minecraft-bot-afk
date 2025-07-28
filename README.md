# Bot Minecraft AFK - Guide de lancement et personnalisation

## Description

Bot Minecraft simple utilisant mineflayer (Node.js) qui reste AFK, affiche le chat en console et se reconnecte automatiquement.

## Personnalisation

Modifie les paramètres directement dans `bot.js` ou passe-les en argument :

```bash
node bot.js <host> <port> <username>
````

Exemple :

```bash
node bot.js survie-mn3F.aternos.me 53623 MonBot
```

## Installation

1. Installer Node.js : [https://nodejs.org](https://nodejs.org)
2. Installer la dépendance mineflayer :

```bash
npm install mineflayer
```

## Lancement

### Sous Windows (PowerShell ou CMD)

```bash
node bot.js <host> <port> <username>
```

Ou via Python :

```bash
python launch_bot.py
```

### Sous Linux/macOS (Terminal)

```bash
node bot.js <host> <port> <username>
```

Ou via Python :

```bash
python3 launch_bot.py
```

## Remarques

* Node.js doit être dans le PATH.
* Python n’est utile que pour lancer via `launch_bot.py`.
* Le bot se reconnecte automatiquement en cas de déconnexion.
