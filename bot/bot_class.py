import re
from telegram import Update, Bot as Bot_init
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from typing import Callable


class Bot:
    def __init__(self, token: str):
        self.__bot = Bot_init(token=token)
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def add_command(self, command_name: str, callback: Callable[[Update, CallbackContext], None]):
        self.dispatcher.add_handler(CommandHandler(command_name, callback))

    def add_msg_handler(self, callback: Callable[[Update, CallbackContext], None], regexp=re.compile(r'.*', re.IGNORECASE)):
        self.dispatcher.add_handler(MessageHandler(
            Filters.text & (~Filters.command) & Filters.regex(regexp),
            callback
        ))

    def start_polling(self):
        self.updater.start_polling()
