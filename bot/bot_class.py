import re
from copy import deepcopy
from telegram import Update, Bot as Bot_init
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from typing import Callable


class Bot:
    def __init__(self, token: str, initial_storage=None):
        self.__bot = Bot_init(token=token)
        self.__updater = Updater(token=token, use_context=True)
        self.__dispatcher = self.__updater.dispatcher
        self.__bot_storage = initial_storage or {}

    def add_command(self, command_name: str, callback: Callable[[Update, CallbackContext], None]):
        self.__dispatcher.add_handler(CommandHandler(command_name, callback))

    def add_msg_handler(self, callback: Callable[[Update, CallbackContext], None], regexp=re.compile(r'.*', re.IGNORECASE)):
        self.__dispatcher.add_handler(MessageHandler(
            Filters.text & (~Filters.command) & Filters.regex(regexp),
            callback
        ))

    def start_polling(self):
        self.__updater.start_polling()

    def get_storage_state(self):
        return deepcopy(self.__bot_storage)

    def save_to_storage(self, key, value):
        self.__bot_storage[key] = value

    def reset_storage(self):
        self.__bot_storage = {}
