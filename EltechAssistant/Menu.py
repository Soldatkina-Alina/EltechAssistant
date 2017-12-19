from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import misc
token = misc.token

MAIN_MENU, SHEDULE, GROUP, TEACHERS, SUBJECTS, EVENTS= range(6)

def start(bot, update):
    reply_keyboard = [['Расписание', 'Группа', 'Преподаватели', 'Предметы', 'Мероприятия']]

    update.message.reply_text(
        'Привет. Я твой помошник. Выбери, что хочешь узнать. Для выхода введи команду /cancel',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, row_wight=1, resize_keyboard=True ))
    return MAIN_MENU

def main_menu(bot, update):
    user = update.message.from_user
    text = update.message.text
    reply_keyboard1 = [['Вся неделя', 'Неделя 1', 'Неделя 2', 'На завтра', 'На сегодня', 'Экзамены', 'Назад']]
    reply_keyboard2 = [['Список группы', 'Почта группы', 'Персона', 'Телефоны', 'Дни рождения', 'Ссылки в Вк', 'Назад']]
    reply_keyboard3 = [['Список преподавателей', 'Персона', 'Назад']]
    reply_keyboard4 = [['Учебный план', 'Преподаватели', 'Предмет', 'Назад']]
    reply_keyboard5 = [['Все мероприятия', 'Назад']]
    if 'Расписание' in text:
        update.message.reply_text('Вы выбрали ' + text,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard1, resize_keyboard=True))
        return SHEDULE
    elif 'Группа' in text:
        update.message.reply_text('Вы выбрали ' + text,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard2, resize_keyboard=True))
        return GROUP
    elif 'Преподаватели' in text:
        update.message.reply_text('Вы выбрали ' + text,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard3, resize_keyboard=True))
        return TEACHERS
    elif 'Предметы' in text:
        update.message.reply_text('Вы выбрали ' + text,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard4, resize_keyboard=True))
        return SUBJECTS
    elif 'Мероприятия' in text:
        update.message.reply_text('Вы выбрали ' + text,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard5, resize_keyboard=True))
        return EVENTS
    elif 'Назад' in text:
        return start(bot, update)
    else:
        pass

def shedule(bot, update):
    text = update.message.text
    update.message.reply_text('Вы выбрали ' + text)
    if 'Вся неделя' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Неделя 1' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Неделя 2' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'На завтра' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'На сегодня' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Экзамены' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Назад' in text:
        return start(bot, update)
    else:
        pass

def group(bot, update):
    text = update.message.text
    update.message.reply_text('Вы выбрали ' + text)
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
        return start(bot, update)
    else:
        pass

def teachers(bot, update):
    text = update.message.text
    update.message.reply_text('Вы выбрали ' + text)
    if 'Список преподавателей' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Персона' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Назад' in text:
        return start(bot, update)
    else:
        pass

def subjects(bot, update):
    text = update.message.text
    update.message.reply_text('Вы выбрали ' + text)
    if 'Учебный план' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Преподаватели' in text:
        return start(bot, update)
    elif 'Предмет' in text:
        return start(bot, update)
    elif 'Назад' in text:
        return start(bot, update)
    else:
        pass

def events (bot, update):
    text = update.message.text
    update.message.reply_text('Вы выбрали ' + text)
    if 'Все мероприятия' in text:
        update.message.reply_text('Вы выбрали ' + text)
        return ''
    elif 'Назад' in text:
        return start(bot, update)
    else:
        pass

def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""

def main():
    updater = Updater(token)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            MAIN_MENU:[RegexHandler('^(Расписание|Группа|Преподаватели|Мероприятия)$', main_menu)],
            SHEDULE:[RegexHandler('^(Вся неделя|Неделя 1|Неделя 2|На завтра|На сегодня|Экзамены|Назад)$', shedule)],
            GROUP:[RegexHandler('^(Список группы|Почта группы|Персона|Телефоны|Дни рождения|Ссылки в Вк|Назад)$', group)],
            TEACHERS:[RegexHandler('^(Список преподавателей|Персона|Назад)$', teachers)],
            SUBJECTS:[RegexHandler('^(Учебный план|Преподаватели|Предмет|Назад)&', subjects)],
            EVENTS: [RegexHandler('^(Название мероприятия|Назад)$', events)]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()
if __name__ == '__main__':
    main()