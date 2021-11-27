
from telebot_creds.credentials import bot
from next_step_handlers import NextStepHandlers
#handlers= Next_Step_Handlers(message)


class CallbackQueries:
    @bot.callback_query_handler(lambda query: query.data == "order_product")
    def callback_order_product(query):
        msg = bot.send_message(query.message.chat.id, " Please enter the Product ID! ")
        bot.register_next_step_handler(msg , NextStepHandlers.check_order_id)

    @bot.callback_query_handler(lambda query: query.data == "review_product")
    def callback_review_product(query):
        bot.send_message(query.message.chat.id, " Choose order to submit review! ")
   
    @bot.callback_query_handler(lambda query: query.data == "order_chosen_product")
    def callback_review_product(query):
        bot.send_message(query.message.chat.id, NextStepHanlders.verify_order_with_agent)

    @bot.callback_query_handler(lambda query: query.data == "check_order_status")
    def callback_check_order_status(query):
        bot.send_message(query.message.chat.id, " Choose order to check status")

    @bot.callback_query_handler(lambda query: query.data == "complaints")
    def callback_complaints(query):
        bot.send_message(query.message.chat.id, " How can we help you? ")

    @bot.callback_query_handler(lambda query: query.data == "choose_language")
    def callback_choose_language(query):
        bot.send_message(query.message.chat.id, " Please choose language below! ")

    @bot.callback_query_handler(lambda query: query.data == "cancel_order")
    def callback_cancel_order(query):
        bot.send_message(query.message.chat.id, " Choose order to cancel ")

    @bot.callback_query_handler(lambda query: query.data == "rules")
    def callback_rules(query):
        bot.send_message(query.message.chat.id, " General Rules ")

    @bot.callback_query_handler(lambda query: query.data == "help")
    def callback_help(query):
        bot.send_message(query.message.chat.id, " All helpful information ")
