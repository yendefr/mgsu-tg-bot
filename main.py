import psycopg2
from telebot import TeleBot, types

from config import BOT_TOKEN
from config import DB_USER, DB_DATABASE, DB_PASSWORD, DB_HOST


bot = TeleBot(BOT_TOKEN)
conn = psycopg2.connect(user=DB_USER,
                        database=DB_DATABASE,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port="5432")
cursor = conn.cursor()


@bot.message_handler(content_types=['document'])
def get_document_info(message):
    print(message.document.file_id)


@bot.message_handler(commands=['timetable', 'files', 'tasks'])
def get_commands(message):
    if message.text == '/timetable':
        send_timetable(message)
    elif message.text == '/files':
        send_files_menu(message)
    elif message.text == '/tasks':
        send_files_menu(message)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет, от меня ты можешь получить расписание занятий и полезные файлы. Также время от времени я буду присылать тебе рассылку всяких важностей!")
    bot.send_message(message.from_user.id, "Для начала, как твоё имечко?")
    bot.register_next_step_handler(message, get_name)


@bot.message_handler(content_types=['text'])
def get_request(message):
    if message.text == 'Расписание':
        send_timetable(message)
    elif message.text == 'Файлы':
        send_files_menu(message)
    elif message.text == 'Домашка':
        send_tasks(message)


def get_name(message):
    name = message.text
    cursor.execute('INSERT INTO students(id, name) VALUES (%s, %s);', (message.from_user.id, name))
    conn.commit()

    bot.send_message(message.from_user.id, 'А фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    surname = message.text
    cursor.execute('UPDATE students SET surname = %s WHERE id = %s;', (surname, message.from_user.id))
    conn.commit()

    buttons = set_buttons((
        ['1', '2'],
    ))

    bot.send_message(message.from_user.id, text='Группа?', reply_markup=buttons)
    bot.register_next_step_handler(message, get_group_number)


def get_group_number(message):
    group_number = message.text
    cursor.execute('UPDATE students SET group_number = %s WHERE id = %s;', (group_number, message.from_user.id))
    conn.commit()

    cursor.execute('SELECT name, surname, group_number FROM students WHERE id = %s;', (message.from_user.id, ))
    user = cursor.fetchone()

    buttons = set_buttons((
        ['Да', 'Нет'],
    ))

    bot.send_message(message.from_user.id, f'Ты {user[0]} {user[1]} из {user[2]} группы, верно?', reply_markup=buttons)
    bot.register_next_step_handler(message, checker)


def send_timetable(message):
    timetable = [
            types.InputMediaPhoto(open('./timetable/tuesday.png', 'rb'), caption='Вот твоё расписание!'),
            types.InputMediaPhoto(open('./timetable/wednesday.png', 'rb')),
            types.InputMediaPhoto(open('./timetable/thursday.png', 'rb')),
            types.InputMediaPhoto(open('./timetable/friday.png', 'rb')),
        ]

    bot.send_media_group(message.from_user.id, timetable)


@bot.message_handler(content_types=['text'])
def get_tasks(message):
    pass


@bot.message_handler(content_types=['text'])
def send_tasks(message):
    pass


def send_files_menu(message):
    if message.text == 'Файлы' or message.text == '/files' or message.text == 'Назад':
        buttons = set_buttons((
            ['Учебники', 'Тетради'],
            ['Презентации', 'Задачники'],
            ['ГДЗ'],
            ['В меню'],
        ))

        bot.send_message(message.from_user.id, 'Что тебе нужно в этот раз?', reply_markup=buttons)
        bot.register_next_step_handler(message, send_files_menu)
    elif message.text == 'В меню':
        set_menu(message)
    else:
        buttons = set_buttons((
            ['Вышмат', 'Инженерная графика', 'Физика'],
            ['🧪Химия', 'История', '🪴Экология'],
            ['🇬🇧Английский язык'],
            ['Назад', 'В меню'],
        ))

        bot.send_message(message.from_user.id, 'Какие тебе нужны?', reply_markup=buttons)
        bot.register_next_step_handler(message, send_files, message.text)


def send_files(message, category):
    if message.text == 'Файлы' or message.text == '/files' or message.text == 'Назад' or message.text == 'В меню':
        send_files_menu(message)
    else:
        subject = message.text

        cursor.execute('SELECT id, name FROM files WHERE category = %s and subject = %s', (category, subject))
        files = cursor.fetchall()

        if not files:
            bot.send_message(message.from_user.id, 'Такого у нас пока нет!')
        else:
            for file_id, name in files:
                bot.send_document(message.from_user.id, data=file_id, caption=name)

        bot.register_next_step_handler(message, send_files, category)


def checker(message):
    if message.text == 'Да':
        bot.send_message(message.from_user.id, text='Круто, теперь можешь потыкать кнопки!')
        set_menu(message)
    elif message.text == 'Нет':
        cursor.execute(f'DELETE FROM students WHERE id = {message.from_user.id};')
        conn.commit()
        
        remove_buttons = types.ReplyKeyboardRemove()

        bot.send_message(message.from_user.id, text='Окей, давай заново. Как тебя зовут, слоупок?', reply_markup=remove_buttons)
        bot.register_next_step_handler(message, get_name)


def set_menu(message):
    buttons = set_buttons((['Расписание', 'Файлы'], ['Получить домашку', 'Записать домашку']))
    bot.send_message(message.from_user.id, text='Вот меню, выбирай что тебе угодно!', reply_markup=buttons)


def set_buttons(buttons_lists: tuple):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for buttons_list in buttons_lists:
        buttons.add(*list(map(types.KeyboardButton, buttons_list)))
    return buttons


bot.polling(none_stop=True, interval=0)
