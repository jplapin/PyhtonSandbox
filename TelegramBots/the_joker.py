from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests, random


#Created the event Handler. Constantly polling for new messages
updater = Updater(token="RemovedForSecurityReasons")

#add new event handlers
dispatcher = updater.dispatcher

def choices(bot, update):
    options = [
        [InlineKeyboardButton("Reddit Jokes",callback_data="redditjokes"),
         InlineKeyboardButton("Stupid Stuff", callback_data="stupidstuff"),
         InlineKeyboardButton("Wocka", callback_data="wocka")
        ]
    ]
    reply = InlineKeyboardMarkup(options)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Choose a type of Joke : ",
                     reply_markup= reply)


dispatcher.add_handler(CommandHandler("jokes", choices))

def joker(bot, update):
    data = update.callback_query.data
    joke = ""
    if data == "redditjokes":
        request = requests.get(
            "https://raw.githubusercontent.com/taivop/joke-dataset/master/reddit_jokes.json")
        rand = random.randint(0, 195000)
        joke = request.json()[rand]["title"]+"\n"+request.json()[rand]["body"]
    elif data == "stupidstuff":
        request = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json")
        rand = random.randint(0, 3770)
        joke = request.json()[rand]["title"]+"\n"+request.json()[rand]["body"]
    elif data == "wocka":
        request = requests.get(
            "https://raw.githubusercontent.com/taivop/joke-dataset/master/wocka.json")
        rand = random.randint(0, 10000)
        joke = request.json()[rand]["title"]+"\n"+request.json()[rand]["body"]

    bot.edit_message_text(chat_id=update.callback_query.message.chat_id, 
                          text = joke,
                          message_id=update.callback_query.message.message_id)


dispatcher.add_handler(CallbackQueryHandler(joker))

#start polling messages
updater.start_polling()

#necessary to use crtl+c to terminate the program in the command line
updater.idle()
