# import everything
from flask import Flask, request
import telegram
import telebot
#from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telebot.credentials import bot_token, bot_user_name,URL
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)
   print (update)
   
   updater = Updater(TOKEN, use_context=True)


   updater.dispatcher.add_handler(CallbackQueryHandler(button))
   chat_id = update.message.chat.id
   msg_id = update.message.message_id
   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
        # print the welcoming message
        bot_welcome = """
        Welcome to coolAvatar bot, the bot is an agent which gives items free for review.
        """
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
        keyboard = [
            [telegram.InlineKeyboardButton("\U0001F4EB Order Product", callback_data='1')],
            [telegram.InlineKeyboardButton("\U0001F31F Review Product", callback_data='2')],
            [telegram.InlineKeyboardButton("\U0001F50D Check Order Status", callback_data='3')],
            [telegram.InlineKeyboardButton("\U0001F44E Complaints", callback_data='4')],
            [telegram.InlineKeyboardButton("\U0001F30F Choose Language", callback_data='5')],
            [telegram.InlineKeyboardButton("\U000026D4 Cancel the Order", callback_data='6')],
            [telegram.InlineKeyboardButton("\U000026A0 Rules", callback_data='7')],
            [telegram.InlineKeyboardButton("\U0001F4E3 Help", callback_data='8')],
            
        ]

        reply_markup = telegram.InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)
   else:
       try:
           # clear the message we got from any non alphabets
           text = re.sub(r"\W", "_", text)
           # create the api link for the avatar based on http://avatars.adorable.io/
           url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
           # reply with a photo to the name the user sent,
           # note that you can send photos by url and telegram will fetch it for you
           bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
       except Exception:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'


def button(context: CallbackContext) -> None:
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'

    
if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
