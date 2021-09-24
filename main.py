from telebot import TeleBot, types
from config import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, от меня ты можешь получить расписание занятий и полезные файлы. Также время от времени я буду присылать тебе рассылку всяких важностей!")
        bot.send_message(message.from_user.id, "Для начала, как твоё имечко?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /help')


def get_name(message):
    global name #TODO: Сделать запись в csv, вместо глобалов
    name = message.text
    bot.send_message(message.from_user.id, 'А фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text

    buttons = set_buttons(['1', '2'])

    bot.send_message(message.from_user.id, text='Группа?', reply_markup=buttons)
    bot.register_next_step_handler(message, get_group)


def get_group(message):
    global group
    group = message.text
    
    buttons = set_buttons(['Да', 'Нет'])

    bot.send_message(message.from_user.id, f'Ты {name} {surname} из {group} группы, верно?', reply_markup=buttons)
    bot.register_next_step_handler(message, checker)


def checker(message):
    buttons = set_buttons(['Расписание', 'Файлы'])
    remove_buttons = types.ReplyKeyboardRemove()

    if message.text == 'Да':
        bot.send_message(message.from_user.id, text='Круто, теперь можешь потыкать кнопки!', reply_markup=buttons)
    elif message.text == 'Нет':
        bot.send_message(message.from_user.id, text='Окей, давай заново. Как тебя зовут, слоупок?', reply_markup=remove_buttons)
        bot.register_next_step_handler(message, get_name)


def set_buttons(buttons_list):
    buttons = types.ReplyKeyboardMarkup()
    for button in buttons_list:
        buttons.add(types.KeyboardButton(button))
    return buttons


bot.polling(none_stop=True, interval=0)
