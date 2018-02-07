import postgresql.driver as pg_driver
import datetime
from EltechAssistant import Prettyfier

db = pg_driver.connect(user='postgres', password='', host='localhost', database='postgres', port=5432)
login = '4373leti@gmail.com'
password = '4373eltech4373'

class FindInDataBase:
    @staticmethod
    def access(text):
        data = db.query("SELECT name FROM public.students WHERE telegramid LIKE " + "'" + str(text) + "'")
        return data if data else 0

    @staticmethod
    def write_telegramid(phone_number, telegramid):
        db.query("UPDATE Students SET TelegramID = " + str(telegramid) + " WHERE students.phonenumber LIKE " + "'" + str(phone_number)+ "'")
        return 0

    @staticmethod
    def find_student_in_group_list(text):
        data = db.query("SELECT name FROM public.students WHERE phonenumber LIKE " + "'" + str(text) + "'")
        return data if data else 0

    @staticmethod
    def shedule (text):
        now = datetime.datetime.now()
        today = now.date()
        date = datetime.datetime.isocalendar(today)
        number_week = date[1]
        number_day = date[2]
        print(date)
        print (number_day)
        print(number_week)
        if (number_week % 2) == 0:
            number_week = 2
            print(number_week)
        else:
            number_week = 1
            print(number_week)
        if 'Все расписание' in text:
            data = db.query("WITH p AS (SELECT DayOfWeek, LessonNumber, 0 as weektype, Subject, Type, Classroom, TeachersSurname, TeachersName FROM TimetableBoth UNION (SELECT DayOfWeek, LessonNumber, 1 as weektype, Subject, Type, Classroom, TeachersSurname, TeachersName FROM TimetableFirst ) UNION (SELECT DayOfWeek, LessonNumber, 2 as weektype, Subject, Type, Classroom, TeachersSurname, TeachersName FROM TimetableSecond s) ORDER BY DayOfWeek, LessonNumber, weektype) SELECT p.DayOfWeek, l.BeginTime, l.EndTime, weektype, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name")
            print(data)
            return Prettyfier.Prettyfier.get_read_of_none(data)
        elif 'Неделя 1' in text:
            data = db.query("WITH p AS (SELECT * FROM TimetableBoth UNION (SELECT * FROM TimetableFirst) ORDER BY DayOfWeek, LessonNumber)SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name;")
            print (data)
            return Prettyfier.Prettyfier.shedule(data)
        elif 'Неделя 2' in text:
            data = db.query("WITH p AS (SELECT * FROM TimetableBoth UNION (SELECT * FROM TimetableSecond) ORDER BY DayOfWeek, LessonNumber)SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name;")
            return Prettyfier.Prettyfier.shedule(data)
        elif 'На завтра' in text:
            number_day = number_day + 1
            print(number_day)
            if number_day == 7:
                number_day = 1
            if number_week == 1:
                print(number_week)
                data = db.query("WITH p AS (SELECT * FROM TimetableBoth WHERE DayOfWeek =" + str(number_day) + " UNION (SELECT * FROM TimetableFirst WHERE DayOfWeek =" + str(number_day) + ") ORDER BY DayOfWeek, LessonNumber) SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name" )
                # print(date)
                return Prettyfier.Prettyfier.shedule(data)
            if number_week == 2:
                print(number_week)
                data = db.query("WITH p AS (SELECT * FROM TimetableBoth WHERE DayOfWeek ="+ str(number_day) + " UNION (SELECT * FROM TimetableSecond WHERE DayOfWeek =" + str(number_day) + ") ORDER BY DayOfWeek, LessonNumber) SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name")
                return Prettyfier.Prettyfier.shedule(data)
        elif 'На сегодня' in text:
            if number_week == 1:
                data = db.query("WITH p AS (SELECT * FROM TimetableBoth WHERE DayOfWeek =" + str(number_day) + " UNION (SELECT * FROM TimetableFirst WHERE DayOfWeek =" + str(number_day) + ") ORDER BY DayOfWeek, LessonNumber) SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name" )
                print(data)
                return Prettyfier.Prettyfier.shedule(data)
            if number_week == 2:
                data = db.query("WITH p AS (SELECT * FROM TimetableBoth WHERE DayOfWeek ="+ str(number_day) + " UNION (SELECT * FROM TimetableSecond WHERE DayOfWeek =" + str(number_day) + ") ORDER BY DayOfWeek, LessonNumber) SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name")
                return Prettyfier.Prettyfier.shedule(data)
        elif 'Экзамены' in text:
            pass

    @staticmethod
    def group (text):
        if 'Список группы' in text:
            data = db.query("SELECT Surname, Name, Patronymic FROM public.students")
            return Prettyfier.Prettyfier.get_read_of_none(data)
        elif 'Почта группы' in text:
            return str("Почта  " + login + "\nПароль  " + password)
        elif 'Телефоны' in text:
            data = db.query("SELECT surname, name, phonenumber FROM public.students")
            return Prettyfier.Prettyfier.get_read_of_none(data)
        elif 'Дни рождения' in text:
            data = db.query("SELECT surname, name, dateofbirth FROM public.students")
            print(data)
            return Prettyfier.Prettyfier.get_read_of_none(data)
        elif 'Ссылки в Вк' in text:
            data = db.query("SELECT surname, name, vklink FROM public.students")
            return Prettyfier.Prettyfier.get_read_of_none(data)

    @staticmethod
    def group_one_person(name):
        data = db.query("SELECT Surname, Name, Patronymic, DateOfBirth, PhoneNumber, VKLink, StudentCardNumber FROM public.students WHERE name like "+ "'%" +name + "%'" + "or surname like" + "'%" +name + "%'" )
        print(str(data))
        return Prettyfier.Prettyfier.one_object(data)

    @staticmethod
    def teachers(name):
        data = db.query("SELECT Surname, Name, Patronymic, Subject FROM  public.Teachers ORDER BY Subject")
        print(str(data))
        return Prettyfier.Prettyfier.one_object(data)

    @staticmethod
    def teachers_one_person(name):
        data = db.query("SELECT * FROM public.teachers WHERE Surname like "+ "'%" + name + "%'" + "or name like" + "'%" +name + "%'")
        print(str(data))
        return Prettyfier.Prettyfier.get_read_of_none(data)

    @staticmethod
    def subjects(text):
        if 'Учебный план' in text:
            data = db.query("SELECT Name, Exam, Coursework, LectureHours, LaboratoryHours, PracticeHours FROM public.Subjects ")
            print(data)
            print(str(data))
            return Prettyfier.Prettyfier.study_plan(data)
        elif 'Преподаватели' in text:
            data = db.query("SELECT Subject, Surname, Name, Patronymic FROM Teachers ORDER BY Subject ")
            print(str(data))
            return Prettyfier.Prettyfier.one_object(data)

    @staticmethod
    def subjects_one_subject(text):
        subject = text.lower()
        print(subject)
        array1 = ['исис', 'инфсис', 'инфокомсис']
        array2 = ['кг', 'компг']
        array3 = ['бд', 'техннбд', 'тбд']
        array4 = ['мс', 'модельсис']
        array5 = ['по', 'тпо', 'трпо']
        array6 = ['мисзи', 'мисиз', 'мисис']
        array7 = ['интелис', 'иис']
        if subject in array1:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Инфокоммуникационные системы и сети'")
            print(data)
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in array2:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Компьютерная графика'")
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in array3:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Технологии баз данных'")
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in array4:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Моделирование систем'")
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in array5:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Технологии разработки ПО'")
            print(data)
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in array6:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Методы и средства защиты информации'")
            print(data)
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in array7:
            data = db.query("SELECT * FROM public.subjects WHERE name like 'Интеллектуальные информационные системы'")
            print(data)
            return Prettyfier.Prettyfier.single_subject(data)
        elif subject in 'бжд':
            data = db.query("SELECT * FROM public.subjects WHERE name like 'БЖД'")
            print(data)
            return Prettyfier.Prettyfier.single_subject(data)
        else:
            return ''

    def events(text):
        data = db.query("Select * from public.Events WHERE DateTime > current_timestamp")
        print(str(data))
        return Prettyfier.Prettyfier.one_object(data)

def main():
#     data = db.query("""WITH p AS (SELECT * FROM TimetableBoth WHERE DayOfWeek = 1
#            UNION (SELECT * FROM TimetableFirst WHERE DayOfWeek = 1)
#            ORDER BY DayOfWeek, LessonNumber)
# SELECT p.DayOfWeek, l.BeginTime, l.EndTime, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic
# FROM p
# LEFT JOIN Lessons l on p.LessonNumber = l.Number
# LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name;
#     """)
#     print(data)
    # data = [('Бертыш', 'Вадим', 'Андреевич'), ('Восканян', 'Виктор', 'Каренович'), ('Середнюк', 'Антон', None)]
    # print(type(data[2][2]))
    # data = db.query(
    #     "WITH p AS (SELECT DayOfWeek, LessonNumber, 0 as weektype, Subject, Type, Classroom, TeachersSurname, TeachersName FROM TimetableBoth UNION (SELECT DayOfWeek, LessonNumber, 1 as weektype, Subject, Type, Classroom, TeachersSurname, TeachersName FROM TimetableFirst) UNION (SELECT DayOfWeek, LessonNumber, 2 as weektype, Subject, Type, Classroom, TeachersSurname, TeachersName FROM TimetableSecond s) ORDER BY DayOfWeek, LessonNumber, weektype) SELECT p.DayOfWeek, l.BeginTime, l.EndTime, weektype, p.Subject, p.Type, p.Classroom, t.Surname, t.Name, t.Patronymic FROM p LEFT JOIN Lessons l on p.LessonNumber = l.Number LEFT JOIN Teachers t on p.TeachersSurname = t.Surname and p.TeachersName = t.Name")
    # print(data)
    # print(data[0][2])
    # print(type(data[0][2]))
    # print(type(data[0]))
    # array = ['Понедельник', 'Вторник', 'Четверг', 'Пятница']
    # j=0
    # res = ''
    # data = list(map(lambda x: tuple(filter(lambda y : not (y is type(True)) ,
    #                                        x)),
    #                 data))
    # for i in range(len(data)):
    #     res +=  ' ' + ' '.join(tuple(map(lambda x: str(x), data[i]))) + '\n'
    #
    # print(res)
    # f = True
    # print(type(f))
    # print(type(bool))
    # for (f, i, o) in data:
    #     res += str(j) + ' ' + f + ' ' + i;
    #     j += 1
    #     if (type(o) == str):
    #         res += ' ' + o
    #     res += '\n'


    # string = str(data)
    # line = re.sub('[,\'\(\)None\]\[]', '', string)
    # myString = []
    # print(line)
    # for i in range (col):
    #     t = (len(str(data[i])))
    #     print(len(str(data[i])))
    #     for j in range (t+1):
    #         if j == t:
    #             myString = line.rjust(t)
    #         else: continue
    # print (myString)
    # for u in range (col):
    #     sentence = "\n ".join(data[u])
    #     print(sentence)

    # d = str(data[0])
    # line = re.sub('[,\'\(\)None\]\[]', '', str(data))
    # print(line)
    # myString = ' '.join(str(data))
    # print (myString)
    # print(len(str(data[1])))

    # data2 = re.split("[,\'\[\]() ]+", str(data))
    # print(data2)
    # for i in range(0, int(len(data2) - 1) // 3):
    #     if data2[i * 3 + 3] != "None":
    #         print(data2[1 + i * 3] + " " + data2[i * 3 + 2] + " " + data2[i * 3 + 3])
    # else:
    #     print(data2[1 + i * 3] + " " + data2[i * 3 + 2])
    pass
if __name__ == '__main__':
   main()
