"""
file: migrations/eltechassistant_20171216_01_HciRp.py
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""CREATE TABLE Students
            (
                StudentCardNumber INT PRIMARY KEY,
                Surname VARCHAR(30) NOT NULL ,
                Name VARCHAR(20) NOT NULL,
                Patronymic VARCHAR(30),
                DateOfBirth DATE NOT NULL,
                PhoneNumber VARCHAR(12) CHECK (PhoneNumber like '+7__________'),
                VKLink VARCHAR(50) CHECK (VKLink like 'https://vk.com/%'),
                Nickname VARCHAR(10) NOT NULL UNIQUE,
                Role INT NOT NULL
            );
    """),
    step("""CREATE TABLE Subjects
            (
                Name VARCHAR(60) PRIMARY KEY,
                Exam BOOLEAN NOT NULL,
                Coursework BOOLEAN NOT NULL,
                LectureHours INT,
                LaboratoryHours INT,
                PracticeHours INT,
                Link VARCHAR(200),
                FilesLink VARCHAR(200),
                Information VARCHAR(5000)
            );
    """),
    step("""CREATE TABLE Teachers
            (
                Surname VARCHAR(30),
                Name VARCHAR(20),
                Patronymic VARCHAR(30),
                Subject VARCHAR(60) NOT NULL REFERENCES Subjects(Name) ON DELETE CASCADE ON UPDATE CASCADE,
                PhoneNumber VARCHAR(12) CHECK (PhoneNumber like '+7__________'),
                Email VARCHAR(30) CHECK (Email similar to '%@%.%'),
                VKLink VARCHAR(50) CHECK (VKLink like 'https://vk.com/%'),
                Information VARCHAR(5000),
                PRIMARY KEY (Surname, Name)
            );
    """),
    step("""CREATE TABLE Lessons
            (
                Number INT PRIMARY KEY,
                BeginTime TIME NOT NULL,
                EndTime TIME NOT NULL
            );
    """),
    step("""CREATE TABLE Exams
            (
                Subject VARCHAR(60) PRIMARY KEY REFERENCES Subjects(Name)  ON DELETE CASCADE ON UPDATE CASCADE,
                DateTime TIMESTAMP NOT NULL,
                Classroom INT,
                TeahersSurname VARCHAR(30) NOT NULL,
                TeachersName VARCHAR(20) NOT NULL,
                FOREIGN KEY (TeahersSurname, TeachersName) REFERENCES Teachers(Surname, Name) ON DELETE CASCADE ON UPDATE CASCADE
            );
    """),
    step("""CREATE TABLE Events
            (
                Name VARCHAR(100) PRIMARY KEY,
                DateTime TIMESTAMP NOT NULL,
                Place VARCHAR(100) NOT NULL,
                Link VARCHAR(200),
                Information VARCHAR(5000)
            );
    """),
    step("""CREATE TABLE TimetableBoth
            (
                DayOfWeek int CHECK (DayOfWeek >= 1 and DayOfWeek <= 6),
                LessonNumber INT REFERENCES Lessons(Number) ON DELETE CASCADE ON UPDATE CASCADE,
                Subject VARCHAR(60) NOT NULL REFERENCES Subjects(Name) ON DELETE CASCADE ON UPDATE CASCADE,
                Type VARCHAR(12) NOT NULL CHECK (Type = 'Лекция' or Type = 'Практика' or Type = 'Лабораторная'),
                Classroom INT,
                TeachersSurname VARCHAR(30),
                TeachersName VARCHAR(20),
                PRIMARY KEY (DayOfWeek, LessonNumber),
                FOREIGN KEY (TeachersSurname, TeachersName) REFERENCES Teachers (Surname, Name) ON DELETE CASCADE ON UPDATE CASCADE
            );
    """),
    step("""CREATE TABLE TimetableFirst
            (
                DayOfWeek int CHECK (DayOfWeek >= 1 and DayOfWeek <= 6),
                LessonNumber INT REFERENCES Lessons(Number) ON DELETE CASCADE ON UPDATE CASCADE,
                Subject VARCHAR(60) NOT NULL REFERENCES Subjects(Name) ON DELETE CASCADE ON UPDATE CASCADE,
                Type VARCHAR(12) NOT NULL CHECK (Type = 'Лекция' or Type = 'Практика' or Type = 'Лабораторная'),
                Classroom INT,
                TeachersSurname VARCHAR(30),
                TeachersName VARCHAR(20),
                PRIMARY KEY (DayOfWeek, LessonNumber),
                FOREIGN KEY (TeachersSurname, TeachersName) REFERENCES Teachers (Surname, Name) ON DELETE CASCADE ON UPDATE CASCADE
            );
    """),
    step("""CREATE TABLE TimetableSecond
            (
                DayOfWeek int CHECK (DayOfWeek >= 1 and DayOfWeek <= 6),
                LessonNumber INT REFERENCES Lessons(Number) ON DELETE CASCADE ON UPDATE CASCADE,
                Subject VARCHAR(60) NOT NULL REFERENCES Subjects(Name) ON DELETE CASCADE ON UPDATE CASCADE,
                Type VARCHAR(12) NOT NULL CHECK (Type = 'Лекция' or Type = 'Практика' or Type = 'Лабораторная'),
                Classroom INT,
                TeachersSurname VARCHAR(30),
                TeachersName VARCHAR(20),
                PRIMARY KEY (DayOfWeek, LessonNumber),
                FOREIGN KEY (TeachersSurname, TeachersName) REFERENCES Teachers (Surname, Name) ON DELETE CASCADE ON UPDATE CASCADE
            );
    """),
    step("""CREATE FUNCTION stop_insert_update_both() RETURNS trigger AS $$
            BEGIN
            IF (SELECT exists(SELECT *
                            FROM TimetableFirst
                            WHERE TimetableFirst.DayOfWeek = NEW.DayOfWeek and TimetableFirst.LessonNumber = NEW.LessonNumber))
            IS TRUE THEN
            RAISE EXCEPTION 'Нельзя добавить значения, уже существующие в таблице TimetableFirst';
            END IF;
            IF (SELECT exists(SELECT *
                            FROM TimetableSecond
                            WHERE TimetableSecond.DayOfWeek = NEW.DayOfWeek and TimetableSecond.LessonNumber = NEW.LessonNumber))
            IS TRUE THEN
            RAISE EXCEPTION 'Нельзя добавить значения, уже существующие в таблице TimetableSecond';
            END IF;
            RETURN NEW;
            END;
        $$ LANGUAGE plpgsql;
    """),
    step("""CREATE FUNCTION stop_insert_update_first_or_second() RETURNS trigger AS $$
            BEGIN
            IF (SELECT exists(SELECT *
                            FROM TimetableBoth
                            WHERE TimetableBoth.DayOfWeek = NEW.DayOfWeek and TimetableBoth.LessonNumber = NEW.LessonNumber))
            IS TRUE THEN
            RAISE EXCEPTION 'Нельзя добавить значения, уже существующие в таблице TimetableBoth';
            END IF;
            RETURN NEW;
            END;
        $$ LANGUAGE plpgsql;
    """),
    step("""CREATE TRIGGER stop_insert_update_both BEFORE INSERT OR UPDATE ON TimetableBoth
                FOR EACH ROW EXECUTE PROCEDURE stop_insert_update_both();
            CREATE TRIGGER stop_insert_update_first BEFORE INSERT OR UPDATE ON TimetableFirst
                FOR EACH ROW EXECUTE PROCEDURE stop_insert_update_first_or_second();
            CREATE TRIGGER stop_insert_update_second BEFORE INSERT OR UPDATE ON TimetableSecond
                FOR EACH ROW EXECUTE PROCEDURE stop_insert_update_first_or_second();    
    """)
]
