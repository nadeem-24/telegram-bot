# python 3
# main.py - contains the source code for the bot

# Important Imports

from email import message
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import api
import bse

updater = Updater(api.BOT_API, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('''Welcome to BSE_infobot.Please type /commands to know valild list of commands.''')

def gainers(update: Update, context: CallbackContext):
    update.message.reply_text(bse.Data.top_gainers())

def losers(update: Update, context: CallbackContext):
    update.message.reply_text(bse.Data.top_losers())

def command(update: Update, context: CallbackContext):
    update.message.reply_text('''/gainers -> get a list of today's top gainers
    /losers -> get a list of today's top losers''')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('gainers', gainers))
updater.dispatcher.add_handler(CommandHandler('losers', losers))
updater.dispatcher.add_handler(CommandHandler('command', command))

updater.start_polling()


