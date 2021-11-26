from telebot_creds.credentials import bot
# from db import conn 
from models.Product import Product
from config import db
class NextStepHandlers:
    def check_order_id(message):
        try:
            chat_id = message.chat.id
            id = message.text
            if not id.isdigit():
                msg = bot.reply_to(message, 'Please enter a number. Try again please')
                bot.register_next_step_handler(msg, NextStepHandlers.check_order_id)
                return
            else:
                product = db.session.query(Product).filter(Product.id==id)[0]
                print(product)
                msg = bot.reply_to(message, product)

                msg = bot.reply_to(message, product.name)
            #bot.register_next_step_handler(msg, process_sex_step)
        except Exception as e:
            bot.reply_to(message, str(e)) 