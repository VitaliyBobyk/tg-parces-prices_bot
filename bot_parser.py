import telebot
from telebot import types
from room import AppleRoom
from ipeople import Ipeople
import sched, time
import requests


room = AppleRoom()
people = Ipeople()


bot = telebot.TeleBot('1125107113:AAGbCs5VnJw5xmfzBDIMWir95ktR24fl9k4')
upd = bot.get_updates()


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Привіт, я бот який допоможе тобі оперативно дізнатись ціни конкурентів :)')


@bot.message_handler(commands=['start'])
def start_message(message):
    user_markup = types.InlineKeyboardMarkup(row_width=2)
    button_room = types.InlineKeyboardButton(text='Apple Room', callback_data='Apple Room')
    button_people = types.InlineKeyboardButton(text='iPeople', callback_data='iPeople')
    user_markup.add(button_room, button_people)
    bot.send_message(message.chat.id, 'Вибери кантору', reply_markup=user_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'mainmenu':
        user_markup = types.InlineKeyboardMarkup(row_width=2)
        button_room = types.InlineKeyboardButton(text='Apple Room', callback_data='Apple Room')
        button_people = types.InlineKeyboardButton(text='iPeople', callback_data='iPeople')
        user_markup.add(button_room, button_people)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Вибери кантору', reply_markup=user_markup)

    if call.data == 'Apple Room':
        user_markup = types.InlineKeyboardMarkup()
        room_new = types.InlineKeyboardButton(text='New', callback_data='room_new')
        room_used = types.InlineKeyboardButton(text='Used', callback_data='room_used')
        backbutton = types.InlineKeyboardButton(text='В меню', callback_data='mainmenu')
        user_markup.add(room_new, room_used, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Обери тип техніки:', reply_markup=user_markup)

    if call.data == 'iPeople':
        user_markup = types.InlineKeyboardMarkup()
        people_new = types.InlineKeyboardButton(text='New', callback_data='people_new')
        people_used = types.InlineKeyboardButton(text='Used', callback_data='people_used')
        backbutton = types.InlineKeyboardButton(text='В меню', callback_data='mainmenu')
        user_markup.add(people_new, people_used, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Обери тип техніки:', reply_markup=user_markup)
    elif call.data == 'room_new':
        user_markup = types.InlineKeyboardMarkup(row_width=2)
        backbutton = types.InlineKeyboardButton(text='В меню', callback_data='mainmenu')
        user_markup.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=room.new())
        bot.send_message(chat_id=call.message.chat.id, text='Назад', reply_markup=user_markup)
    elif call.data == 'room_used':
        user_markup = types.InlineKeyboardMarkup(row_width=2)
        backbutton = types.InlineKeyboardButton(text='В меню', callback_data='mainmenu')
        user_markup.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=room.used())
        bot.send_message(chat_id=call.message.chat.id, text='Назад', reply_markup=user_markup)
    elif call.data == 'people_new':
        user_markup = types.InlineKeyboardMarkup(row_width=2)
        backbutton = types.InlineKeyboardButton(text='В меню', callback_data='mainmenu')
        user_markup.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=people.new())
        bot.send_message(chat_id=call.message.chat.id, text='Назад', reply_markup=user_markup)
    elif call.data == 'people_used':
        user_markup = types.InlineKeyboardMarkup(row_width=2)
        backbutton = types.InlineKeyboardButton(text='В меню', callback_data='mainmenu')
        user_markup.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=people.used())
        bot.send_message(chat_id=call.message.chat.id, text='Назад', reply_markup=user_markup)


bot.polling()
