from termcolor import colored

import numpy


class Players:
    def __init__(self, filepath='../rsc/Players.txt'):
        self.__tag = colored('Players', 'yellow')
        self.__raw_data = numpy.genfromtxt(fname=filepath, dtype='str', delimiter='\n')
        self.__results = self.__raw_data.copy().tolist()
        self.__void = 0
        for i in range(len(self.__raw_data)):
            if len(self.__raw_data[i]) > self.__void:
                self.__void = len(self.__raw_data[i])

    def process(self, processes):
        count_format = len(str(len(self.__results)))
        print('\n ' + count_format * ' ' + self.__tag)
        order = 1
        for result in self.__results:
            print(colored(f'{order:0{count_format}}', "green"), end=' ')
            order += 1
            for process in processes:
                process(result)

    def order(self):
        self.__tag = colored('Order', 'yellow')
        self.__results = self.__raw_data.copy()
        numpy.random.shuffle(self.__results)

    def versus(self):
        self.__tag = colored('Versus', 'yellow')
        players = self.__raw_data.copy()
        numpy.random.shuffle(players)

        self.__results = []
        for i in range(0, len(players) - 1, 2):
            self.__results.append(f'{players[i]:<{self.__void}}{colored(" versus ", "green")}{players[i + 1]}')

        if len(players) % 2 == 1:
            self.__results.append(f'{players[len(players) - 1]} is waiting..')

    def free_for_all(self):
        self.__tag = colored('Free4All', 'yellow')

        self.__results = []
        for i in range(len(self.__raw_data)):
            for j in range(0, i):
                self.__results.append(f'{self.__raw_data[i]:<{self.__void}}{colored(" versus ", "green")}{self.__raw_data[j]}')

        numpy.random.shuffle(self.__results)

    def groups(self, count=4):
        self.__tag = colored('Groups', 'yellow')
        players = self.__raw_data.copy()
        numpy.random.shuffle(players)
        self.__results = []
        index = 0
        group = ''
        for player in players:
            group += player + ', '
            index += 1
            if index == count:
                self.__results.append(group[:-2])
                group = ''
                index = 0

        if group:
            self.__results.append(group[:-2])
