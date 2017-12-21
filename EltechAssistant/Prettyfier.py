import re

week = {1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота',
        7: 'Воскресенье'}

class Prettyfier:

    def get_read_of_none(data):
        result = ''
        print(data)
        data = list(map(lambda x: tuple(filter(lambda y: not (y is None),
                                               x)),
                        data))
        for i in range(len(data)):
            result += str(i + 1)+ '.' + ' ' + ' '.join(tuple(map(lambda x: str(x), data[i]))) + '\n'

        print(result)
        return result

    def shedule(data):
        result = ''
        data = list(map(lambda x: tuple(filter(lambda y: not (y is None),
                                               x)),
                        data))
        # days = list(map(lambda x: week[x[0]], data))
        for (d, dtb, dte, n, t, r, f, i, o) in data:
            result += week[d] + ': ' + ' '.join(tuple(map(lambda x: str(x), (dtb, dte, n, t, r, f, i, o)))) + '\n'
        # for i in range(len(data)):
        #     result +=  ' '.join(tuple(map(lambda x: str(x), data[i]))) + '\n'
        print(result)
        return result

    def one_object(data):
        result = ''
        data = list(map(lambda x: tuple(filter(lambda y: not (y is None),
                                               x)),
                        data))
        for i in range(len(data)):
            result += ' '.join(tuple(map(lambda x: str(x), data[i]))) + '\n'
        print(result)
        return result

    @staticmethod
    def study_plan(data):
        result = ''
        for (n, e, k, t, tt, z) in data:
            result += n + ' '
            if e:
                result += 'Экзамен есть '
            else:
                result += 'Диф зачет '
            if k:
                result += 'Курсовая работа есть '
            else:
                result += 'Курсовой работы нет '
            foo = tuple(filter(lambda y: not (y is None), (t, tt, z)))
            foo = tuple(map(str, foo))
            bar = ' '.join(foo) + '\n'
            result += bar
        print(result)
        return result
