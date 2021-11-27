from app import app
from flask import request
from callbacks import CallbackQueries
from telebot_creds.credentials import bot, TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Update

CallbackQueries()

@bot.message_handler(commands=['start'])
def start(message):
    bot_welcome = """
        Welcome to coolAvatar bot, the bot is an agent which gives items free for review.
        """
        # send the welcoming message
    bot.reply_to(message, text=bot_welcome)
    bot.send_message(message.chat.id,"Please choose:", reply_markup=start_markup())

@bot.message_handler(commands=['order_chosen_product'])
def start(message):
    bot_welcome = """
        Welcome to coolAvatar bot, the bot is an agent which gives items free for review.
        """
        # send the welcoming message
    bot.reply_to(message, text=bot_welcome)
    bot.send_message(message.chat.id,"Please choose:", reply_markup=start_markup())


def start_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    markup.add(InlineKeyboardButton("\U0001F4EB Order Product", callback_data='order_product'),
            InlineKeyboardButton("\U0001F31F Review Product", callback_data='review_product'),
            InlineKeyboardButton("\U0001F50D Check Order Status", callback_data='check_order_status'),
            InlineKeyboardButton("\U0001F44E Complaints", callback_data='complaints'),
            InlineKeyboardButton("\U0001F30F Choose Language", callback_data='choose_language'),
            InlineKeyboardButton("\U000026D4 Cancel the Order", callback_data='cancel_order'),
            InlineKeyboardButton("\U000026A0 Rules", callback_data='rules'),
            InlineKeyboardButton("\U0001F4E3 Help", callback_data='help'))
    return markup

""" @bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    print(message)
    bot.reply_to(message, message.text) """


#b.callback_order_product()
#bot.send_message(query.message.chat.id, " Please enter the Product ID! ")




@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://b751-5-197-201-227.ngrok.io/' + TOKEN)
    return "!", 200


