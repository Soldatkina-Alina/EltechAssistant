import unittest

from EltechAssistant.Prettyfier import Prettyfier


class MyTestCase(unittest.TestCase):
    def test_format_list_of_tuples(self):
        in_data = [('Бертыш', 'Вадим', 'Андреевич'), ('Восканян', 'Виктор', 'Каренович'), ('Середнюк', 'Антон', None)]
        res = Prettyfier.get_read_of_none(in_data)

        out_true = "1. Бертыш Вадим Андреевич\n2. Восканян Виктор Каренович\n3. Середнюк Антон\n"
        out_false = "1. Бертыш Вадим Андреевич\n2. Восканян Виктор Каренович\n3. Середнюк Антон None\n"
        self.assertEqual(res, out_true)
        self.assertNotEqual(res, out_false)

    def test_shedule(self):
        in_data = [(3,'11:40:00', '13:15:00', 'Зимнее солнцестояние', 'колдунство', 2121, 'Йольский', 'Кот','СожралВсех'), (3, '13:45:00', '15:20:00', 'Компьютеграя графика', 'Лекция', 42, 'Ктулху', 'Рльех', 'Фхтагн')]
        res = Prettyfier.shedule(in_data)

        out_true = "Среда: 11:40:00 13:15:00 Зимнее солнцестояние колдунство 2121 Йольский Кот СожралВсех\nСреда: 13:45:00 15:20:00 Компьютеграя графика Лекция 42 Ктулху Рльех Фхтагн\n"
        self.assertEqual(res, out_true)

    def test_one_object(self):
        in_data = [('Просто','нужно', 'чтобы','лямбда','склеила','все','эти','строки','и', None, 'не', 'только', 42, None)]
        res = Prettyfier.one_object(in_data)

        out_true = "Просто нужно чтобы лямбда склеила все эти строки и не только 42\n"
        self.assertEqual(res, out_true)

    def test_study_plan(self):
        in_data = [('Зельеварение', True, False, 100500, 999, None), ('Wizzard run', False, True, 42, 0, 22)]
        res = Prettyfier.study_plan(in_data)

        out_true = "Зельеварение Экзамен есть Курсовой работы нет 100500 999\nWizzard run Диф зачет Курсовая работа есть 42 0 22\n"
        self.assertEqual(res,out_true)


if __name__ == '__main__':
    unittest.main()
