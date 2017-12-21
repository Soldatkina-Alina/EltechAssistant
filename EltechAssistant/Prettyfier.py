import re
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
        for i in range(len(data)):
            result +=  ' '.join(tuple(map(lambda x: str(x), data[i]))) + '\n'
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

    def study_plan(data):
        result = ''
        for (n, e, k, t, tt, z) in data:
            if data[e] == True:
                data[e] = 'Экзамен есть'
            else:
                data[e] = 'Экзамена нет'
        for (n, e, k, t, tt) in data:
            if data[k] == True:
                data[k] = 'Курсовая работа есть'
            else:
                data[k] = 'Курсовой работы нет'
        data = list(map(lambda x: tuple(filter(lambda y: not (y is None),
                                               x)),
                        data))
        for i in range(len(data)):
            result += ' '.join(tuple(map(lambda x: str(x), data[i]))) + '\n'
        print(result)
        return result