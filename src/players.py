import numpy


class Players:
    def __init__(self, filepath='../rsc/Players.txt'):
        self.__tag = '[Players]'
        self.__raw_data = numpy.genfromtxt(fname=filepath, dtype='str', delimiter='\n')
        self.__results = self.__raw_data.copy().tolist()

        self.__void = 0
        for i in range(len(self.__raw_data)):
            if len(self.__raw_data[i]) > self.__void:
                self.__void = len(self.__raw_data[i])

    def process(self, processes):
        print()
        print(self.__tag)
        order = 1
        count_format = len(str(len(self.__results)))
        for result in self.__results:
            print(str(f'{order:0{count_format}d}'), end=') ')
            order += 1
            for process in processes:
                process(result)

    def order(self):
        self.__tag = '[Order]'
        self.__results = self.__raw_data.copy()
        numpy.random.shuffle(self.__results)

    def versus(self):
        self.__tag = '[Versus]'
        players = self.__raw_data.copy()
        numpy.random.shuffle(players)

        result = []
        for i in range(0, len(players) - 1, 2):
            result.append(f'{players[i]:<{self.__void}} versus {players[i + 1]}')

        if len(players) % 2 == 1:
            result.append('{player} is waiting..'.format(player=players[len(players) - 1]))

        self.__results = result

    def free_for_all(self):
        self.__tag = '[Free4All]'

        result = []
        for i in range(len(self.__raw_data)):
            for j in range(0, i):
                result.append(f'{self.__raw_data[i]:<{self.__void}} versus {self.__raw_data[j]}')

        numpy.random.shuffle(result)
        self.__results = result

    def groups(self, count=4):
        self.__tag = '[Groups]'
        players = self.__raw_data.copy()
        numpy.random.shuffle(players)
        result = []
        index = 0
        group = ''
        for player in players:
            group += player + ', '
            index += 1
            if index == count:
                result.append(group[:-2])
                group = ''
                index = 0

        if group:
            result.append(group[:-2])

        self.__results = result
