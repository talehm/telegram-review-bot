from telebot_creds.credentials import bot
# from db import conn 
# from config import db
class NextStepHandlers:
    def check_order_id(message):
        try:
            chat_id = message.chat.id
            id = message.text
            print(age)
            if not id.isdigit():
                msg = bot.reply_to(message, 'Please enter a number. Try again please')
                bot.register_next_step_handler(msg, NextStepHandlers.check_order_id)
                return
            else:
                msg = bot.reply_to(message, 'Thank you')
            #bot.register_next_step_handler(msg, process_sex_step)
        except Exception as e:
            bot.reply_to(message, str(e)) 