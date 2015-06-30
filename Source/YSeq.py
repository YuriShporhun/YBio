class YSeq:
    """This class represents a sequence"""

    #The sequence of the letters of an alphabet
    _sequence = []

    #Constructor makes a copy of sequence
    def __init__(self, sequence):
        """Constructor constructs sequence as list
        :param sequence: the sequence of the letters of some alphabet
        :type sequence: str
        """
        self._sequence = sequence[:]
    
    def Count(self, symbol):
        """This method returns the number of characters in the sequence as int
        :param symbol: symbol or sequence of some alphabet
        """
        return self._sequence.count(symbol)

    def Append(self, symbol):
        '''This method adds a character or sequence
        symbol: symbol or sequence of some alphabet
        '''
        self._sequence.extend(symbol)

    def Save(self, filename, separator = ''):
        '''This method saves a sequence in the file
        filename: is path to the file
        separator: is a string which will added to each symbol in the sequence
        '''
        with open(filename, 'w') as file:
            for item in self._sequence: file.write(str(item) + separator)

    def __repr__(self):
        return ''.join(self._sequence)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self._sequence)

    def __getitem__(self, index):
        return self._sequence[index]

    def Load(self, filename):
        '''This method loads a sequence from file
        filename: is path to the file
        '''
        with open(filename) as file:
            [self._sequence.extend(x.rstrip('\n')) for x in file]

    def LongestCommonSubstring(self, sequence):
        pass
