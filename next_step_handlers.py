from telebot_creds.credentials import bot
# from db import conn 

from app.models import Product
from app import db


class NextStepHandlers:
    def check_order_id(self, message):
        try:
            message_id = message.message_id
            chat_id = message.chat.id
            id = message.text
            print(id)
            if not id.isdigit():
                msg = bot.reply_to(message, 'Please enter a number. Try again please')
                bot.register_next_step_handler(msg, NextStepHandlers.check_order_id)
                return
            else:
                product = db.session.query(Product).filter(Product.id==id)[0]
                # msg = bot.reply_to(message, type(product))
                msg = bot.send_photo(chat_id, photo='https://www.thewechatagency.com/wp-content/uploads/2017/11/chat_bot-01-660x495.jpg', caption=product.name, reply_to_message_id=message_id)
                # msg = bot.reply_to(message,  reply_markup=self.order_chosen_product_markup())
                msg = bot.send_message(chat_id, "Please choose:", reply_markup=order_chosen_product_markup())

                # msg = bot.reply_to(message, product.name)
            #bot.register_next_step_handler(msg, process_sex_step)
        except IndexError as e:
            msg = bot.reply_to(message, "Product ID not found!")
        except Exception as e:
            bot.reply_to(message, str(e)) 

    def verify_order_with_agent(self,message):
        try:
            message_id=message.message_id
            chat_id=message.chat.id
            msg = bot.reply_to(message, "Please send your paypal email and amazon profile link. Please fuck off if you do not have Ayten")
        except Exception as e:
            print(str(e))
            bot.reply_to(message, str(e)) 

@bot.callback_query_handler(lambda query: query.data == "order_chosen_product")
def callback_order_chosen_product(query):
    bot.send_message(query.message.chat.id, NextStepHandlers.verify_order_with_agent)


def order_chosen_product_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    markup.add(InlineKeyboardButton("\U0001F4EB Order This Product", callback_data='order_chosen_product'))
    return markup 