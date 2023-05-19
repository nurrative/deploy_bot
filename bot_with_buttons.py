import telebot
from decouple import config

token = config('TOKEN')

#стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBW1kBYbPTAcqdWM-xeSzuB4LEMV25QACaQAD_DykE9Y6t3D0xHBILgQ'
no_sticker = 'CAACAgIAAxkBAAEIBXdkBYbbUd74_HVKOaOe8soLBsY-FgACewAD_DykE864AAHndwzFIC4E'

bot = telebot.TeleBot(token)

#клавиатура, которая будет находиться там, где клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('Да')
b2 = telebot.types.KeyboardButton('Нет')
keyboard.add(b1,b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)
# register_next_step_handler - принимает сообщение и функцию, которая вызовется как только пользователь отправит любое сообщение
# это сообщение и передастся в функцию

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')
    bot.register_next_step_handler(message, reply_to_button)

bot.polling()