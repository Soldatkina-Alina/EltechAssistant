class Prettyfier:
    def get_read_of_none(data):
        result = ''
        data = list(map(lambda x: tuple(filter(lambda y: type(y) == str,
                                               x)),
                        data))
        for i in range(len(data)):
            result += str(i + 1) + ' ' + ' '.join(data[i]) + '\n'
        print(result)
        return result