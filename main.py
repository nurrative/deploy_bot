import telebot
from decouple import config
# config - функция, которая достает значение переменной в файле .env (пример, как должен выглядеть файл .env в файле .env - эта фунция позволяет в ДАННОМ СЛУЧАЕ не показывать на виду наш ключ Токен)


token = config('TOKEN')

bot = telebot.TeleBot(token)  #запускаем нашего бота

@bot.message_handler(commands=['start'])
# декоратор message_handler нужен, чтобы реагировать на определенные сообщения, данный декоратор уже встроен в bot (?)

# commands - встроенный параметр, представляющий список команд (функция работает, когда ползователь написал одну из них)


def start_message(message):
    bot.send_message(message.chat.id, 'Hello')  #вместо "message.chat.id" можно написать  892891195
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBRZkBXYLzRtuLYx8tQglxiZQ0WJ9_AACDQYAAtCG-wqBWgG-gkiB_S4E')
    bot.send_photo(message.chat.id, 'https://ru.freepik.com/free-photo/lavender-field-at-sunset-near-valensole_35758793.htm#query=landscape&position=0&from_view=keyword&track=sph')

#message.chat.id - встроенный параметр, который позволяет вывести какое то сообщение, которое записано во 2 аргументе. И выводит такое сообщение только в том чате, в котором мы указали, благодаря "chat.id"

#не нужно вызывать функцию, так как сама программа автоматичесвки понимает, что нужно это сдедать, благодаря импортирования библиотеки telebot или благодаря Telegram API

@bot.message_handler(content_types=['text'])
# content_types - список типов сообщений (text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message, web_app_data)

# content_types=['text'] - функция будет работать, когда пользователь отправил обычное сообщение
# content_types=['audio'] - работает, когда отправил айдио сообщение
def aaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет")
    else:
        bot.send_message(message.chat.id, "Сообщение не распознано")

@bot.message_handler(content_types=['sticker'])
def bbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)

bot.polling()


