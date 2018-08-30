from telegram.ext import Updater, MessageHandler, Filters

#Created the event Handler. Constantly polling for new messages
updater = Updater(token="RemovedForSecurityReasons")

#add new event handlers
dispatcher = updater.dispatcher

def echo(bot,update):
    update.message.reply_text(update.message.text)

dispatcher.add_handler(MessageHandler(Filters.text, echo))

#start polling messages
updater.start_polling()

#necessary to use crtl+c to terminate the program in the command line
updater.idle()
