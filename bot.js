const mineflayer = require('mineflayer');

const HOST = process.argv[2] || 'survie-mn3F.aternos.me';
const PORT = parseInt(process.argv[3]) || 53623;
const USERNAME = process.argv[4] || 'BotPersonnalise';

function createBot() {
  const bot = mineflayer.createBot({
    host: HOST,
    port: PORT,
    username: USERNAME,
  });

  bot.on('spawn', () => {
    console.log(`Bot connecté sur ${HOST}:${PORT} en tant que ${USERNAME}`);
  });

  bot.on('end', () => {
    console.log('Déconnecté, reconnexion dans 5s...');
    setTimeout(createBot, 5000);
  });

  bot.on('error', err => {
    console.log('Erreur:', err);
  });

  bot.on('chat', (username, message) => {
    console.log(`[CHAT] ${username}: ${message}`);
  });
}

createBot();
