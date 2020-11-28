from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from bot import Bot


def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def msg_with_keyboard(update: Update, context: CallbackContext):
    reply_keyboard = [['Confirm', 'Restart']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    context.bot.send_message(chat_id=update.effective_chat.id, text='Как дела?', reply_markup=markup)


BOT_TOKEN = '1412832721:AAFsug46EX33UFUFh0Zfky8l0kp6Q5WfiVs'
bot = Bot(BOT_TOKEN)
bot.add_command('start', start_command)
bot.add_msg_handler(msg_with_keyboard)
bot.start_polling()
