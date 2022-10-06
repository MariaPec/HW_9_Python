from telegram import Bot 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

 
bot = Bot(token='5672444760:AAHPCUD7LaNQRxIBb7QuVaLzaVi9zHwwLKs') 
updater = Updater(token='5672444760:AAHPCUD7LaNQRxIBb7QuVaLzaVi9zHwwLKs') 
dispatcher = updater.dispatcher 

def DelAbv(a):
    list1 = a.split(" ")
    result = ""
    for i in list1:
        if "абв" not in i:
            result += i + " "
    return result

def deleter(update, context): 
    text = update.message.text 
    
    context.bot.send_message(update.effective_chat.id, f'{DelAbv(text)}') 

dispatcher.add_handler(MessageHandler(Filters.text, deleter))

updater.start_polling()
updater.idle() 
