#!/usr/bin/env python
# -*- coding: utf-8 -*-

class YSeq:
    """
    En: This class represents a sequence
    Ru: Данный класс инкапсулирует произвольную последовательность символов
    """

    #Constructor makes a copy of sequence
    def __init__(self, sequence):
        """
        En: This constructor constructs the sequence as a list
        Ru: Данный конструктор позволяет заполнить хранящуюся последовательность сткокой
        :param sequence: the sequence of the letters of some alphabet
        :type sequence: str
        :raise TypeError: if sequence type isn't str
        """
        if type(sequence) is not str:
            raise TypeError("The sequence type isn't str")

        self._sequence = []
        self.append(sequence)
    
    def count(self, symbol):
        """
        En: This method gets the number of occurrences of the symbol in the sequence
        Ru: Определяет количество вхождений символа symbol в последовательности
        :param symbol: symbol or sequence of some alphabet
        :type symbol: str
        :return: the number of occurrences of the symbol in the sequence
        :rtype: int
        :raise TypeError: if symbol type isn't str
        :raise ValueError: if symbol is an empty string
        """
        if type(symbol) is not str:
            raise TypeError("The symbol type isn't str")

        if not symbol:
            raise ValueError("The symbol is an empty string")

        return self._sequence.count(symbol)

    def append(self, symbol):
        """
        En: This method adds a character or sequence
        Ru: Добавляет символ или строку к последовательности
        :param symbol: symbol or sequence of some alphabet
        :type symbol: str
        """
        self._sequence.extend(symbol)

    def save(self, filename, separator=''):
        """
        This method saves a sequence into the particular file
        :param filename: a path to the file
        :type filename: str
        :param separator: a string which will be added to each symbol in the sequence
        :type separator: str
        """
        with open(filename, 'w') as file:
            for item in self._sequence:
                file.write(item + separator)

    def __repr__(self):
        return ''.join(self._sequence)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self._sequence)

    def __getitem__(self, index):
        return self._sequence[index]

    def load(self, filename):
        """This method loads a sequence from file
        :param filename: is path to the file
        :type filename: str
        """
        with open(filename) as file:
            [self._sequence.extend(x.rstrip('\n')) for x in file]