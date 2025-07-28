import subprocess

HOST = "survie-mn3F.aternos.me"
PORT = "53623"
USERNAME = "BotPersonnalise"

def launch_bot():
    # Lancer le bot Node.js avec les arguments
    subprocess.run(['node', 'bot.js', HOST, PORT, USERNAME])

if __name__ == "__main__":
    launch_bot()
