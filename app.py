import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telebot_creds.credentials import bot, TOKEN
from callbacks import CallbackQueries
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://szlikxxxsncvyh:76df9a0905ef0ef2170da0ac7d9d5889c62f2e83d124f7b37febe03dda5cc376@ec2-54-228-209-117.eu-west-1.compute.amazonaws.com:5432/d2j7i18j7mu6q4'
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#callbacks = CallbackQueries(bot)
# Includes all callback queries
CallbackQueries()


@bot.message_handler(commands=['start'])
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
    bot.set_webhook(url='https://telegram-review-bot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))