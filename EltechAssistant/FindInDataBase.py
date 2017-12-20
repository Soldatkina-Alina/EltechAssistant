import postgresql.driver as pg_driver
import datetime
import re
db = pg_driver.connect(user='postgres', password='', host='localhost', database='postgres', port=5432)

def shedule (text):
    now = datetime.datetime.now()
    today = now.date()
    date = datetime.datetime.isocalendar(today)
    number_week = date[1]
    number_day = date[2]
    if 'Вся неделя' in text:
        data = db.query("")
        return (data)
    elif 'Неделя 1' in text:
        data = db.query("SELECT * FROM public.secondtable WHERE value = '" + 1)
        return str(data)
    elif 'Неделя 2' in text:
        data = db.query("SELECT * FROM public.secondtable WHERE value = '" + 2)
        return str(data)
    elif 'На завтра' in text:
        data = db.query("SELECT * FROM public.secondtable WHERE value = '" + number_week + "and   =" + number_day +1)
        return str(data)
    elif 'На сегодня' in text:
        data = db.query("SELECT * FROM public.secondtable WHERE value = '" + number_week + "and   =" + number_day)
        return str(data)

    elif 'Экзамены' in text:
        pass
def group (text):
    if 'Список группы' in text:
        data = db.query("SELECT Surname, Name, Patronymic FROM public.students")
        return (data)
    elif 'Почта группы' in text:
        data = '4373leti@gmail.com'
        password = '4373eltech4373'
        return str("Почта  " + data + "\nПароль  " + password)
    elif 'Телефоны' in text:
        data = db.query("SELECT surname, name, phonenumber FROM public.students")
        return str(data)
    elif 'Дни рождения' in text:
        data = db.query("SELECT surname, name, dateofbirth FROM public.students")
        print(data)
        return str(data)
    elif 'Ссылки в Вк' in text:
        data = db.query("SELECT surname, name, vklink FROM public.students")
        return str(data)

def group_one_person(name):
    data = db.query("SELECT Surname, Name, Patronymic, DateOfBirth, PhoneNumber, VKLink, StudentCardNumber FROM public.students WHERE name like "+ "'%" +name + "%'" + "or surname like" + "'%" +name + "%'" )
    print(str(data))
    return str(data)

def teachers(name):
    data = db.query("SELECT Surname, Name, Patronymic, Subject FROM  public.Teachers ORDER BY Subject")
    print(str(data))
    return str(data)

def teachers_one_person(name):
    data = db.query("SELECT * FROM public.teachers WHERE Surname like "+ "'%" + name + "%'" + "or name like" + "'%" +name + "%'")
    print(str(data))
    return str(data)

def subjects(text):
    if 'Учебный план' in text:
        data = db.query("SELECT Name, Exam, Coursework, LectureHours, LaboratoryHours, PracticeHours FROM public.Subjects ")
        print(data)
        print(str(data))
        return str(data)
    elif 'Преподаватели' in text:
        data = db.query("SELECT Subject, Surname, Name, Patronymic FROM Teachers ORDER BY Subject ")
        print(str(data))
        return str(data)

def subjects_one_subject(text):
    subject = text.lower()
    array1 = ['исис', 'инфсис', 'инфокомсис']
    array2 = ['кг', 'компг']
    array3 = ['бд', 'техннбд', 'тбд']
    array4 = ['мс', 'модельсис']
    array5 = ['по', 'тпо', 'трпо']
    array6 = ['мисзи', 'мисиз', 'мисис']
    array7 = ['интелис', 'иис']
    if subject in array1:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Инфокоммуникационные системы и сети'")
        return str(data)
    elif subject in array2:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Компьютерная графика'")
        return str(data)
    elif subject in array3:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Технологии баз данных'")
        return str(data)
    elif subject in array4:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Моделирование систем'")
        return str(data)
    elif subject in array5:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Технологии разработки ПО'")
        return str(data)
    elif subject in array6:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Методы и средства защиты информации'")
        return str(data)
    elif subject in array7:
        data = db.query("SELECT * FROM public.subjects WHERE name like 'Интеллектуальные информационные системы'")
        return str(data)
    elif subject in 'бжд':
        data = db.query("SELECT * FROM public.subjects WHERE name like 'БЖД'")
        return str(data)
    else:
        return ''

def events(text):
    date = datetime.date.today()
    print(date)
    data = db.query("Select * from public.Events where" + date +" > datatime")
    print(str(data))
    return str(data)

def main():
    data = [('Бертыщ', 'Вадим', 'Андреевич'), ('Восканян', 'Виктор', 'Каренович'), ('Середнюк', 'Антон', None)]
    data2 = re.split("[,\'\[\]() ]+", str(data))
    print(data2)
    for i in range(0, int(len(data2) - 1) // 3):
        if data2[i * 3 + 3] != "None":
            print(data2[1 + i * 3] + " " + data2[i * 3 + 2] + " " + data2[i * 3 + 3])
    else:
        print(data2[1 + i * 3] + " " + data2[i * 3 + 2])
    pass
if __name__ == '__main__':
   main()