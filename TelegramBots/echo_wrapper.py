import telegram

bot = telegram.Bot(token="RemovedForSecurityReasons")

chats = bot.get_updates()

for chat in chats:
    print(chat.message.text) 
