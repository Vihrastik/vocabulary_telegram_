import random
from collections import defaultdict

import telebot
from telebot import types

from src.const import (
    TOKEN,
    Language,
    END_MESSAGE,
    HINT_MESSAGE,
    NEXT_MESSAGE,
    HAPPY_STICKERS,
    BAD_STICKERS,
    RUS_ENG,
    ENG_RUS,
)
# Инициируем класс для работы с Excel-словарем
from src.excel_loader import ExcelLoader
from src.user_states import UserState, DIRECTION_ANSWER, LANGUAGE_QUESTION, LANGUAGE_ANSWER, TOPIC_ANSWER, \
    TRANSLATION_ANSWER

# Инициируем телеграмм-бота
bot = telebot.TeleBot(TOKEN)

# Добавляем статусы ответов пользователя
USER_STATE = defaultdict(lambda: UserState())
excel_loader = ExcelLoader()


# TODO разделять словари по пользователям

# Получаем статусы ответов пользователя в зависимости от типа сообщения (текстовое или кнопки)
def get_state(message=None, callback_query=None):
    if callback_query:
        message = callback_query.message
    return USER_STATE[message.chat.id].state


# Обновляем статусы ответов пользователя для перехода между действиями
def get_user_state(message=None, callback_query=None):
    message = message or callback_query.message
    return USER_STATE[message.chat.id]


def update_state(message=None, callback_query=None, state=None):
    if callback_query:
        message = callback_query.message
    USER_STATE[message.chat.id] = state


def _send_translation_request(chat_id):
    user_state = USER_STATE[chat_id]
    keyboard = create_keyboard([HINT_MESSAGE, NEXT_MESSAGE, END_MESSAGE])
    bot.send_message(chat_id=chat_id,
                     text=f'Введите перевод "{user_state.get_current_word()}"',
                     reply_markup=keyboard)


def _next_word_or_choose_topic(chat_id, skip):
    user_state = USER_STATE[chat_id]
    if user_state.next_word(skip):
        return True
    # no words left in current topic, need to choose another one
    bot.send_message(chat_id=chat_id, text='В данном топике закончились слова. Нужно выбрать новый.')
    _select_topic(chat_id, user_state.lang)
    return False


def _select_topic(chat_id, lang):
    user_state = USER_STATE[chat_id]
    topics = excel_loader.get_topics(lang)
    keyboard = create_keyboard(topics)
    bot.send_message(chat_id=chat_id,
                     text=f'Какую тему выбрать? Доступные темы:',
                     reply_markup=keyboard)
    user_state.choose_lang(lang)


# Создание клавиатуры для выбора
def create_keyboard(but: list):
    keyboard = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(text=b, callback_data=b) for b in but]
    keyboard.add(*buttons)
    return keyboard


# Получение команды на начало (/start) и вывод доступных языков
@bot.message_handler(func=lambda message: get_state(message=message) == LANGUAGE_QUESTION, commands=['start'])
def handle_LANGUAGE_QUESTION(message):
    keyboard = create_keyboard([Language.eng, Language.fr, Language.ger])
    bot.send_message(chat_id=message.chat.id,
                     text=f'Какой язык выбрать?',
                     reply_markup=keyboard)
    user_state = get_user_state(message=message)
    user_state.wait_language()


# Получение ответа пользователя, какой язык использовать, и вывод доступных тем (excel-вкладок)
@bot.callback_query_handler(func=lambda callback_query: get_state(callback_query=callback_query) == LANGUAGE_ANSWER)
def handle_LANGUAGE_ANSWER(callback_query):
    lang = callback_query.data
    if lang not in [Language.eng, Language.fr, Language.ger]:
        return
    _select_topic(callback_query.message.chat.id, lang)


# Получение ответа пользователя, какую тему использовать, и вывод вариантов направления перевода
@bot.callback_query_handler(func=lambda callback_query: get_state(callback_query=callback_query) == TOPIC_ANSWER)
def handle_TOPIC_ANSWER(callback_query):
    topic = callback_query.data
    user_state = get_user_state(callback_query=callback_query)
    words = excel_loader.get_words(user_state.lang, topic)

    keyboard = create_keyboard([RUS_ENG, ENG_RUS])
    bot.send_message(chat_id=callback_query.message.chat.id,
                     text=f'Выберите направление перевода:\n',
                     reply_markup=keyboard)

    user_state.choose_topic(topic, words)


# Получение ответа пользователя по направлению перевода и вывод рандомного слова для перевода
@bot.callback_query_handler(func=lambda callback_query: get_state(callback_query=callback_query) == DIRECTION_ANSWER)
def handle_DIRECTION_ANSWER(callback_query):
    direction = callback_query.data
    user_state = get_user_state(callback_query=callback_query)
    user_state.choose_direction(direction)

    _send_translation_request(callback_query.message.chat.id)


# Обработка кнопок Дальше, Подсказка
@bot.callback_query_handler(func=lambda callback_query: get_state(callback_query=callback_query) == TRANSLATION_ANSWER)
def handle_russian_word_key(callback_query):
    command = callback_query.data
    chat_id = callback_query.message.chat.id
    if END_MESSAGE in command:
        bot.send_message(chat_id=callback_query.message.chat.id,
                         text='Настройки сброшены. Для тренировки введите /start')
        USER_STATE.pop(chat_id)
        return

    user_state = get_user_state(callback_query=callback_query)
    if command == HINT_MESSAGE:
        bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=f'"{user_state.get_current_word()}" переводится "{user_state.get_current_translation()}"\n'
                 f'[Google переводчик "{user_state.get_current_word()}](https://translate.google.com/?'
                 f'hl=ru#view=home&op=translate&sl=auto&tl=ru&text={user_state.get_foreign_word()})"',
            parse_mode='markdown',
            disable_web_page_preview=True
        )

    user_state.next_word(True)
    _send_translation_request(chat_id)


# Проверка полученного сообщения на перевод слова (с русского на английский)
@bot.message_handler(func=lambda message: get_state(message=message) == TRANSLATION_ANSWER)
def handle_russian_word_answ(message):
    text = message.text
    user_state = get_user_state(message=message)
    if user_state.is_valid_answer(text):
        bot.send_sticker(message.chat.id, random.choice(HAPPY_STICKERS))
        bot.send_message(chat_id=message.chat.id, text='Верно!')
        if not _next_word_or_choose_topic(message.chat.id, False):
            return
    else:
        bot.send_sticker(message.chat.id, random.choice(BAD_STICKERS))
        bot.send_message(chat_id=message.chat.id,
                         text=f'Неправильно! Попробуйте еще раз')
    _send_translation_request(message.chat.id)


# Запуск телеграм-бота
bot.polling(none_stop=True, interval=0)
