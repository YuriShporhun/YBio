class YSeq:
    """This class represents a sequence"""

    #Constructor makes a copy of sequence
    def __init__(self, sequence):
        """
        En: This constructor constructs the sequence as a list
        Ru: ƒанный конструктор позвол€ет заполнить хран€щуюс€ последовательность сткокой
        :param sequence: the sequence of the letters of some alphabet
        :type sequence: str
        """
        if type(sequence) is not str:
            raise TypeError("The sequence type has to be 'str'")

        self._sequence = []
        self.append(sequence)
    
    def count(self, symbol):
        """
        This method returns the number of characters in the sequence as int
        :param symbol: symbol or sequence of some alphabet
        :type symbol: str
        """
        return self._sequence.count(symbol)

    def append(self, symbol):
        """This method adds a character or sequence
        :param symbol: symbol or sequence of some alphabet
        :type symbol: str
        """
        self._sequence.extend(symbol)

    def save(self, filename, separator = ''):
        """This method saves a sequence into the particular file
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