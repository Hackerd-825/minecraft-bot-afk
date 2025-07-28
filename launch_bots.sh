#!/bin/bash
# Lance 3 bots AFK Minecraft en arrière-plan

python3 bot_afk.py BotAFK1 play.example.com 25565 &
python3 bot_afk.py BotAFK2 play.example.com 25565 &
python3 bot_afk.py BotAFK3 play.example.com 25565 &

wait
