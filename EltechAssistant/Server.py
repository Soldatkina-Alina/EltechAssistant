# Main module entry point
from EltechAssistant.Menu import Menu
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import misc

MAIN_MENU, SCHEDULE, GROUP, TEACHERS, SUBJECTS, EVENTS, GROUP_ONE_PERSON,\
    TEACHERS_ONE_PERSON, SUBJECTS_ONE_SUBJECT = range(9)

token = misc.token


class Server:
    @staticmethod
    def start():
        updater = Updater(token)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(

            entry_points=[CommandHandler('start', Menu.start)],

            states={
                MAIN_MENU: [RegexHandler('^(Расписание|Группа|Преподаватели|Предметы|Мероприятия)$', Menu.main_menu)],
                SCHEDULE:
                    [RegexHandler('^(Все расписание|Неделя 1|Неделя 2|На завтра|На сегодня|Экзамены|Назад)$',
                                  Menu.schedule)],
                GROUP:
                    [RegexHandler('^(Список группы|Почта группы|Персона|Телефоны|Дни рождения|Ссылки в Вк|Назад)$',
                                  Menu.group)],
                TEACHERS: [RegexHandler('^(Список преподавателей|Персона|Назад)$', Menu.teachers)],
                SUBJECTS: [RegexHandler('^(Учебный план|Преподаватели|Предмет|Назад)$', Menu.subjects)],
                EVENTS: [RegexHandler('^(Все мероприятия|Назад)$', Menu.events)],
                GROUP_ONE_PERSON: [MessageHandler(Filters.text, Menu.group_one_person)],
                TEACHERS_ONE_PERSON: [MessageHandler(Filters.text, Menu.teachers_one_person)],
                SUBJECTS_ONE_SUBJECT: [MessageHandler(Filters.text, Menu.subjects_one_subject)]



            },

            fallbacks=[CommandHandler('cancel', Menu.cancel)]
        )

        dp.add_handler(conv_handler)

        dp.add_error_handler(Menu.error)

        updater.start_polling()

        updater.idle()


if __name__ == '__main__':
    Server.start()
