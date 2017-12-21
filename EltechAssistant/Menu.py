from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from EltechAssistant.Database import Database

import re

MAIN_MENU, SCHEDULE, GROUP, TEACHERS, SUBJECTS, EVENTS, GROUP_ONE_PERSON, \
    TEACHERS_ONE_PERSON, SUBJECTS_ONE_SUBJECT = range(9)


class Menu:
    @staticmethod
    def start(bot, update):
        reply_keyboard = [['Расписание', 'Группа', 'Преподаватели', 'Предметы', 'Мероприятия']]
        update.message.reply_text(
            'Привет. Я твой помощник. Что ты хочешь у меня узнать? \n Для перезапуска нажми /start \n Для прекращения разговора нажми /cancel',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, row_wight=1, resize_keyboard=True))
        return MAIN_MENU

    @staticmethod
    def init(bot, update):
        reply_keyboard = [['Расписание', 'Группа', 'Преподаватели', 'Предметы', 'Мероприятия']]
        update.message.reply_text(
            'Сделайте ваш следующий выбор! Или нажмите на /cancel',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, row_wight=1, resize_keyboard=True))
        return MAIN_MENU

    @staticmethod
    def main_menu(bot, update):
        user = update.message.from_user
        text = update.message.text

        reply_keyboard1 = [['Все расписание', 'Неделя 1', 'Неделя 2', 'На завтра', 'На сегодня', 'Экзамены', 'Назад']]
        reply_keyboard2 = [
            ['Список группы', 'Почта группы', 'Персона', 'Телефоны', 'Дни рождения', 'Ссылки в Вк', 'Назад']]
        reply_keyboard3 = [['Список преподавателей', 'Персона', 'Назад']]
        reply_keyboard4 = [['Учебный план', 'Преподаватели', 'Предмет', 'Назад']]
        reply_keyboard5 = [['Все мероприятия', 'Назад']]

        global markup
        global res

        if 'Расписание' in text:
            markup = ReplyKeyboardMarkup(reply_keyboard1, resize_keyboard=True)
            res = SCHEDULE
        elif 'Группа' in text:
            markup = ReplyKeyboardMarkup(reply_keyboard2, resize_keyboard=True)
            res = GROUP
        elif 'Преподаватели' in text:
            markup = ReplyKeyboardMarkup(reply_keyboard3, resize_keyboard=True)
            res = TEACHERS
        elif 'Предметы' in text:
            markup = ReplyKeyboardMarkup(reply_keyboard4, resize_keyboard=True)
            res = SUBJECTS
        elif 'Мероприятия' in text:
            markup = ReplyKeyboardMarkup(reply_keyboard5, resize_keyboard=True)
            res = EVENTS
        elif 'Назад' in text:
            return Menu.init(bot, update)

        update.message.reply_text('Вы выбрали ' + text, reply_markup=markup)
        return res

    @staticmethod
    def schedule(bot, update):
        text = update.message.text
        if 'Назад' in text:
            return Menu.init(bot, update)
        else:
            data = Database.shedule(text)
            update.message.reply_text(data, reply_markup=ReplyKeyboardRemove())
            return Menu.init(bot, update)

    @staticmethod
    def group(bot, update):
        text = update.message.text
        if 'Персона' in text:
            update.message.reply_text('Вы выбрали ' + text, reply_markup=ReplyKeyboardRemove())
            return GROUP_ONE_PERSON
        elif 'Назад' in text:
            return Menu.init(bot, update)
        elif 'Список' in text:
            data = Database.group(text)
            update.message.reply_text(data, reply_markup=ReplyKeyboardRemove())
            return Menu.init(bot, update)
        else:
            data = Database.group(text)
            update.message.reply_text(data, reply_markup=ReplyKeyboardRemove())
            return Menu.init(bot, update)

    @staticmethod
    def teachers(bot, update):
        text = update.message.text
        if 'Список преподавателей' in text:
            data = Database.teachers(text)
            update.message.reply_text(data)
            return Menu.init(bot, update)
        elif 'Персона' in text:
            update.message.reply_text('Вы выбрали ' + text, reply_markup=ReplyKeyboardRemove())
            return TEACHERS_ONE_PERSON
        elif 'Назад' in text:
            return Menu.init(bot, update)

    @staticmethod
    def subjects(bot, update):
        text = update.message.text
        if 'Предмет' in text:
            update.message.reply_text('Вы выбрали ' + text, reply_markup=ReplyKeyboardRemove())
            return SUBJECTS_ONE_SUBJECT
        elif 'Назад' in text:
            return Menu.init(bot, update)
        else:
            data = Database.subjects(text)
            update.message.reply_text(data)
            return Menu.init(bot, update)

    @staticmethod
    def events(bot, update):
        text = update.message.text
        if 'Все мероприятия' in text:
            data = Database.events(text)
            update.message.reply_text(data, reply_markup=ReplyKeyboardRemove())
            return Menu.init(bot, update)
        elif 'Назад' in text:
            pass
        return Menu.init(bot, update)

    @staticmethod
    def group_one_person(bot, update):
        text = update.message.text
        data = Database.group_one_person(text)
        update.message.reply_text(data)
        return Menu.init(bot, update)

    @staticmethod
    def teachers_one_person(bot, update):
        text = update.message.text
        data = Database.teachers_one_person(text)
        update.message.reply_text(data)
        return Menu.init(bot, update)

    @staticmethod
    def subjects_one_subject(bot, update):
        text = update.message.text
        data = Database.subjects_one_subject(text)
        update.message.reply_text(data)
        return Menu.init(bot, update)

    @staticmethod
    def cancel(bot, update):
        update.message.reply_text('Пока! \n'
                                  'Для запуска нажми /start',
                                  reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END

    @staticmethod
    def error(bot, update, error):
        """Log Errors caused by Updates."""
