#знаю, что проект слабый, но у меня было мало времени, из за учебы ничего не успеваю(((
import telebot
from info import help_message, about_message, N1_Text, level_1_text, answers, Answers_1, Answers_2, Answer_all, finals3, final1, final2, quest2, start_message
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
token = "6843217225:AAHCjKE26lam0HeEZ96v2BuBReMnkGPRQWM"
bot = telebot.TeleBot(token=token)
global user_data
user_data = {}

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('/start - запустить бота'))
markup.add(KeyboardButton('/quest - начать квест'))
markup.add(KeyboardButton('/about - о квесте'))
markup.add(KeyboardButton('/help - узнать что умеет бот'))


@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text = help_message)



@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}!\n"
                                      f"Чтобы начать проходить квест прост тыкай сюда -> /quest\n"
                                      f"Если хочешь узнать, что умеет бот нажми -> /help ", reply_markup = markup)
    global chat_id
    chat_id = message.chat.id
    if chat_id not in user_data:
        user_data[chat_id] = {}
        if "lvl" not in user_data[chat_id]:
            user_data[chat_id]["lvl"] = 0
            print(user_data)
        if "loc" not in user_data[chat_id]:
            user_data[chat_id]["loc"] = 0
            print(user_data)
        if "winORlose" not in user_data[chat_id]:
            user_data[chat_id]["winORlose"] = 0

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=help_message, reply_markup = markup)


@bot.message_handler(commands=['about'])
def bot_about(message):
    bot.send_photo(chat_id=message.chat.id, photo="https://avatars.mds.yandex.net/get-images-cbir/4380055/QSxetU190PVTYY_ykSTlEA6783/ocr", caption=about_message, reply_markup=markup)


@bot.message_handler(commands=['quest'], content_types=['text'])
def bot_quest(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Да"))
    markup.add(KeyboardButton("Нет"))
    bot.send_photo(chat_id=message.chat.id, photo="https://avatars.mds.yandex.net/get-images-cbir/3522140/1CauLA9z2OZempjnPY9CtQ6700/ocr", caption= start_message, reply_markup=markup)
    bot.register_next_step_handler(message, bot_quest_1)


def bot_quest_1(message):
    if message.text == "Да":
        if user_data[chat_id]["lvl"] == 0:
            level_1(message)
        elif message.text == "Нет":
            bot.send_message(chat_id=message.chat.id, text=N1_Text, reply_markup=markup)
#добавить фото

def level_1(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Луна'))
    markup.add(KeyboardButton('Солнце'))
    markup.add(KeyboardButton('Звезда'))
    bot.send_photo(chat_id=message.chat.id, photo= "https://avatars.mds.yandex.net/get-images-cbir/1593758/U76MDIOuW4jR6nFTjNo_pw7007/ocr", caption= level_1_text, reply_markup=markup)
    bot.register_next_step_handler(message, lvl1progress)


def lvl1progress(message):
    if message.text == "Луна":
        user_data[chat_id]["lvl"] += 2
        user_data[chat_id]["loc"] += 0
        bot.send_photo(chat_id=message.chat.id,
                       photo="https://avatars.mds.yandex.net/get-images-cbir/1756803/kPmzsxwLZ6tsu7uEEWRQIQ7645/ocr", reply_markup=markup)
        Quest(message)
    if message.text == "Солнце":
        user_data[chat_id]["lvl"] += 1
        user_data[chat_id]["loc"] += 0
        bot.send_photo(chat_id=message.chat.id,
                       photo="https://avatars.mds.yandex.net/get-images-cbir/1020941/u0kQxoKq7_LZduGNfWVtBg7396/ocr", reply_markup=markup)
        Quest(message)
    if message.text == "Звезда":
        bot.send_photo(chat_id=message.chat.id,
                       photo="https://avatars.mds.yandex.net/get-images-cbir/4328881/B4Jo8SUq53qyC9WntC7rWQ8104/ocr",
                       caption=N1_Text, reply_markup=markup)
    if message.text not in answers:
        bot.send_message(message.chat.id, "Некорректный ввод. Выберите е один из вариантов ответа", reply_markup=markup)
        level_1(message)


def Quest(message):
    chat_id
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(Answers_1[user_data[chat_id]["lvl"]][user_data[chat_id]["loc"]]))
    markup.add(KeyboardButton(Answers_2[user_data[chat_id]["lvl"]][user_data[chat_id]["loc"]]))
    bot.send_message(message.chat.id, Answer_all[user_data[chat_id]["lvl"]][user_data[chat_id]["loc"]], reply_markup=markup)
    print(user_data)
    bot.register_next_step_handler(message, progress)


def Quest1(message):
    chat_id
    bot.send_photo(chat_id=message.chat.id,
                   photo="https://avatars.mds.yandex.net/get-images-cbir/1576963/lOCpf2zpzv-h4ChH4q2xog7602/ocr",
                   reply_markup=markup)
    Quest(message)


def Quest2(message):
    chat_id
    bot.send_photo(chat_id=message.chat.id,
                   photo="https://avatars.mds.yandex.net/get-images-cbir/4328881/B4Jo8SUq53qyC9WntC7rWQ8104/ocr",
                   caption=quest2, reply_markup=markup)


def Final(message):
    chat_id
    if user_data[chat_id]["lvl"] == 2:
        bot.send_photo(chat_id= message.chat.id, photo= "https://avatars.mds.yandex.net/get-images-cbir/2473989/rmxH7oiv6-SFTN9TbCjVqg8059/ocr", caption=finals3, reply_markup=markup)


def Final1(message):
    chat_id
    bot.send_photo(chat_id=message.chat.id,
                       photo="https://avatars.mds.yandex.net/get-images-cbir/3750383/Tpvz2mZi77StggrDotxBiQ7287/ocr",caption= final1, reply_markup=markup)


def Final2(message):
    chat_id
    bot.send_photo(chat_id=message.chat.id,
                   photo="https://avatars.mds.yandex.net/get-images-cbir/3611098/B_p1DTz4CF8ivFwySg29Vg8214/ocr",
                   caption=final2, reply_markup=markup)

def progress(message):
    chat_id
    if user_data[chat_id]["lvl"] == 1:
        if message.text == "Забрать":
            user_data[chat_id]["winORlose"] += 1
            Final1(message)
        elif message.text == "Оставить":
            user_data[chat_id]["winORlose"] += 2
            Final2(message)


        elif message.text == "Свет":
            user_data[chat_id]["loc"] += 1
            Quest2(message)
        elif message.text == "Сны":
            user_data[chat_id]["loc"] += 2
            Quest1(message)
        else:
            bot.send_message(message.chat.id, "Введите один из вариантов ответа", reply_markup=markup)
            Quest(message)

    if user_data[chat_id]["lvl"] == 2:
        if message.text == "1":
            user_data[chat_id]["winORlose"] += 1
            Final(message)
        elif message.text == 2:
            user_data[chat_id]["winORlose"] += 2
            Final(message)
        elif message.text == "Забрать":
            user_data[chat_id]["winORlose"] += 3
            Final1(message)
        elif message.text == "Оставить":
            user_data[chat_id]["lvl"] += 4
            Final2(message)

        elif message.text == "Слева":
            user_data[chat_id]["loc"] += 1
            Quest1(message)
        elif message.text == "Справа":
            user_data[chat_id]["winORlose"] += 1
            Final(message)
        else:
            bot.send_message(message.chat.id, "Введите один из вариантов ответа", reply_markup=markup)
            Quest(message)


bot.polling()
