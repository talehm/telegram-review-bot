from telebot_creds.credentials import bot
# from db import conn 
from app.models import Product
from app import db
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
                
                msg = bot.reply_to(message, type(product))
                msg = bot.send_photo(chat_id, photo='https://www.thewechatagency.com/wp-content/uploads/2017/11/chat_bot-01-660x495.jpg')
                msg = bot.reply_to(message, product.name)
            #bot.register_next_step_handler(msg, process_sex_step)
        except IndexError as e:
            msg = bot.reply_to(message, "Product ID not found!")
        except Exception as e:
            bot.reply_to(message, str(e)) 