# Main module entry point
from telegram.ext import Updater, ConversationHandler, CommandHandler, RegexHandler
from EltechAssistant.Menu import Menu

MAIN_MENU, SCHEDULE, GROUP, TEACHERS, SUBJECTS, EVENTS = range(6)



class Server:
    @staticmethod
    def start():
        updater = Updater(token)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', Menu.start)],

            states={
                MAIN_MENU: [RegexHandler('^(Расписание|Группа|Преподаватели|Мероприятия)$', Menu.main_menu)],
                SCHEDULE:
                    [RegexHandler('^(Вся неделя|Неделя 1|Неделя 2|На завтра|На сегодня|Экзамены|Назад)$',
                                  Menu.schedule)],
                GROUP:
                    [RegexHandler('^(Список группы|Почта группы|Персона|Телефоны|Дни рождения|Ссылки в Вк|Назад)$',
                                  Menu.group)],
                TEACHERS: [RegexHandler('^(Список преподавателей|Персона|Назад)$', Menu.teachers)],
                SUBJECTS: [RegexHandler('^(Учебный план|Преподаватели|Предмет|Назад)&', Menu.subjects)],
                EVENTS: [RegexHandler('^(Название мероприятия|Назад)$', Menu.events)]

            },

            fallbacks=[CommandHandler('cancel', Menu.cancel)]
        )

        dp.add_handler(conv_handler)

        dp.add_error_handler(Menu.error)

        updater.start_polling()

        updater.idle()


if __name__ == '__main__':
    Server.start()
