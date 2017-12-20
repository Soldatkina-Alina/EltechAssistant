from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

MAIN_MENU, SCHEDULE, GROUP, TEACHERS, SUBJECTS, EVENTS = range(6)


class Menu:
    @staticmethod
    def start(bot, update):
        reply_keyboard = [['Расписание', 'Группа', 'Преподаватели', 'Предметы', 'Мероприятия']]

        update.message.reply_text(
            'Привет. Для выхода введи команду /cancel',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, row_wight=1, resize_keyboard=True))
        return MAIN_MENU

    @staticmethod
    def init(bot, update):
        reply_keyboard = [['Расписание', 'Группа', 'Преподаватели', 'Предметы', 'Мероприятия']]

        update.message.reply_text(
            'Выбери, что хочешь узнать. Для выхода введи команду /cancel',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, row_wight=1, resize_keyboard=True))
        return MAIN_MENU

    @staticmethod
    def main_menu(bot, update):
        user = update.message.from_user
        text = update.message.text

        reply_keyboard1 = [['Вся неделя', 'Неделя 1', 'Неделя 2', 'На завтра', 'На сегодня', 'Экзамены', 'Назад']]
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
        # update.message.reply_text('Вы выбрали ' + text)
        if 'Вся неделя' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'Неделя 1' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'Неделя 2' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'На завтра' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'На сегодня' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'Экзамены' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'Назад' in text:
            pass

        return Menu.init(bot, update)

    @staticmethod
    def group(bot, update):
        text = update.message.text
        # update.message.reply_text('Вы выбрали ' + text)
        # Next step is "db query => fuzzy search" to get info on specific student
        if 'Список группы' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Почта группы' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Персона' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Телефоны' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Дни рождения' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Ссылки в Вк' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Назад' in text:
            return Menu.init(bot, update)

    @staticmethod
    def teachers(bot, update):
        text = update.message.text
        # update.message.reply_text('Вы выбрали ' + text)
        # Next step is "db query => fuzzy search" to get info on specific student
        if 'Список преподавателей' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Персона' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Назад' in text:
            return Menu.init(bot, update)

    @staticmethod
    def subjects(bot, update):
        text = update.message.text
        update.message.reply_text('Вы выбрали ' + text)
        if 'Учебный план' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Преподаватели' in text:
            update.message.reply_text('Вы выбрали ' + text)
            return ''
        elif 'Предмет' in text:
            return ''
        elif 'Назад' in text:
            return Menu.init(bot, update)

    @staticmethod
    def events(bot, update):
        text = update.message.text
        update.message.reply_text('Вы выбрали ' + text)
        if 'Все мероприятия' in text:
            update.message.reply_text('Вы выбрали ' + text)
        elif 'Назад' in text:
            pass
        return Menu.init(bot, update)

    @staticmethod
    def cancel(bot, update):
        user = update.message.from_user
        update.message.reply_text('Bye! I hope we can talk again some day.',
                                  reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END

    @staticmethod
    def error(bot, update, error):
        """Log Errors caused by Updates."""
