from telebot_creds.credentials import bot
# from db import conn 
from app.models import Product
from app import db
class NextStepHandlers:
    def check_order_id(message):
        try:
            message_id = message.message_id
            chat_id = message.chat.id
            id = message.text
            if not id.isdigit():
                msg = bot.reply_to(message, 'Please enter a number. Try again please')
                bot.register_next_step_handler(msg, NextStepHandlers.check_order_id)
                return
            else:
                product = db.session.query(Product).filter(Product.id==id)[0]
                # msg = bot.reply_to(message, type(product))
                msg = bot.send_photo(chat_id, photo='https://www.thewechatagency.com/wp-content/uploads/2017/11/chat_bot-01-660x495.jpg', caption=product.name, reply_to_message_id=message_id, reply_markup=order_chosen_product_markup()))
                # msg = bot.reply_to(message, product.name)
            #bot.register_next_step_handler(msg, process_sex_step)
        except IndexError as e:
            msg = bot.reply_to(message, "Product ID not found!")
        except Exception as e:
            bot.reply_to(message, str(e)) 
            
    def verify_order_with_agent():
        try:
            message_id=message.message_id
            chat_id=message.chat.id
            msg = bot.reply_to(message, "Please send your paypal email and amazon profile link")
        except:


def order_chosen_product_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    markup.add(InlineKeyboardButton("\U0001F4EB Order This Product", callback_data='order_chosen_product'),
            InlineKeyboardButton("\U0001F31F Return Home", callback_data='return_home'),
    return markup