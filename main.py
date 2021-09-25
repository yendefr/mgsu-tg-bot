from telebot import TeleBot, types
import sqlite3
import json

from config import BOT_TOKEN


bot = TeleBot(BOT_TOKEN)
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет, от меня ты можешь получить расписание занятий и полезные файлы. Также время от времени я буду присылать тебе рассылку всяких важностей!")
    bot.send_message(message.from_user.id, "Для начала, как твоё имечко?")
    bot.register_next_step_handler(message, get_name)


@bot.message_handler(content_types=['text'])
def get_request(message):
    if message.text == 'Расписание':
        send_shedule(message)


def get_name(message):
    name = message.text
    cursor.execute(f'INSERT INTO users(id, name) VALUES ({message.from_user.id}, ?);', (name,))
    conn.commit()

    bot.send_message(message.from_user.id, 'А фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    surname = message.text
    cursor.execute(f'UPDATE users SET surname = ? WHERE id = {message.from_user.id};', (surname,))
    conn.commit()

    buttons = set_buttons(['1', '2'])

    bot.send_message(message.from_user.id, text='Группа?', reply_markup=buttons)
    bot.register_next_step_handler(message, get_group_number)


def get_group_number(message):
    group_number = message.text
    cursor.execute(f'UPDATE users SET group_number = ? WHERE id = {message.from_user.id};', (group_number,))
    conn.commit()

    cursor.execute(f'SELECT name, surname, group_number FROM users WHERE id = {message.from_user.id};')
    user = cursor.fetchone()
    print(user)
    
    buttons = set_buttons(['Да', 'Нет'])

    bot.send_message(message.from_user.id, f'Ты {user[0]} {user[1]} из {user[2]} группы, верно?', reply_markup=buttons)
    bot.register_next_step_handler(message, checker)


def send_shedule(message):
    shedule = [
            types.InputMediaPhoto(open('./shedule/tuesday.png', 'rb'), caption='Вот твоё расписание!'),
            types.InputMediaPhoto(open('./shedule/wednesday.png', 'rb')),
            types.InputMediaPhoto(open('./shedule/thursday.png', 'rb')),
            types.InputMediaPhoto(open('./shedule/friday.png', 'rb')),
        ]

    bot.send_media_group(message.from_user.id, shedule)


def checker(message):
    buttons = set_buttons(['Расписание', 'Файлы'])
    remove_buttons = types.ReplyKeyboardRemove()

    if message.text == 'Да':
        bot.send_message(message.from_user.id, text='Круто, теперь можешь потыкать кнопки!', reply_markup=buttons)
    elif message.text == 'Нет':
        cursor.execute(f'DELETE FROM users WHERE id = {message.from_user.id};')
        conn.commit()

        bot.send_message(message.from_user.id, text='Окей, давай заново. Как тебя зовут, слоупок?', reply_markup=remove_buttons)
        bot.register_next_step_handler(message, get_name)


def set_buttons(buttons_list):
    buttons = types.ReplyKeyboardMarkup()
    for button in buttons_list:
        buttons.add(types.KeyboardButton(button))
    return buttons


bot.polling(none_stop=True, interval=0)
