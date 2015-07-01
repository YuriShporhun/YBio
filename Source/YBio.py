from YSeq import YSeq
from YLoader import YLoader
from YDNA import YDNA
from YRNA import YRNA

class YSeqFunc:

    @staticmethod
    def HammingDistance(seq_one, seq_two):
        """A Static method which calculates the Hamming distance
        between two sequences for
        """
        distance = 0
        for i in range(0, len(seq_one)):
            if seq_one[i] != seq_two[i]:
                distance += 1
        return distance

    @staticmethod
    def TransitionTransversionRatio(seq_one, seq_two):
        """A Static method which calculates the Transiton and
        Transversion ratio
        """
        ratio = 0
        transitions = 0
        transversions = 0
        for i in range(0, len(seq_two)):
            if seq_one[i] != seq_two[i]:
                if (seq_one[i] == 'A' and seq_two[i] == 'G') or \
                   (seq_one[i] == 'C' and seq_two[i] == 'T') or \
                   (seq_one[i] == 'G' and seq_two[i] == 'A') or \
                   (seq_one[i] == 'T' and seq_two[i] == 'C'):
                    transitions += 1
                else:
                    transversions += 1
        return transitions / transversions

class _YServiceMatrix():
    _matrix = []
    _cols = 0
    _rows = 0

    def __init__(self, dna_sequences):
        self._matrix = dna_sequences[:]
        self._cols = self.__Normalize()
        self._rows = len(self._matrix)

    def __Normalize(self):
        max_size = 0
        for seq in range(len(self._matrix)):
            if len(self._matrix[seq]) > max_size:
                max_size = len(self._matrix[seq])

        for seq in range(len(self._matrix)):
            if len(self._matrix[seq]) < max_size:
                self._matrix[seq] += ('_' * (max_size - len(self._matrix[seq])))
        return max_size

    def _Transpose(self):
        self._matrix = [[self._matrix[j][i] for j in range(len(self._matrix))] for i in range(len(self._matrix[0]))]
        self._cols, self._rows = self._rows, self._cols

    def Append(self, sequence):
        self._matrix.append(sequence)
        self._cols = self.__Normalize()
        self._rows += 1

    def GetColCount(self):
        return self._cols

    def GetRowCount(self):
        return self._rows

    def GetItem(self, row, col):
        return self._matrix[row][col]

class YMatrix(_YServiceMatrix):
    def __init__(self, dna_sequences):
        super().__init__(dna_sequences)

    def __repr__(self):
        repr = ''
        for item in self._matrix:
            repr += str(item) + '\n'
        return repr

    def Profile(self):
        profile = YMatrix([])
        for col in range(self._cols):
            temp_dna = YDNA([])
            for row in range(self._rows):
                temp_dna.Append(self._matrix[row][col])
            profile.Append(temp_dna.Count())
        profile._Transpose()
        return profile

    def SaveProfile(self, filename, designations = False):
        indexes = {
            0: 'A',
            1: 'C',
            2: 'G',
            3: 'T'
           }
        profile = self.Profile()
        profile._Transpose()
        sign_flag = True
        with open(filename, 'w') as file:
            for i in range(profile.GetColCount()):
                if designations and sign_flag:
                    file.write(indexes[i] + ': ')
                for j in range(profile.GetRowCount()):
                    file.write(str(profile.GetItem(j, i)) + ' ')
                file.write('\n')

    def SaveConsensus(self, filename):
        consensus = self.Consensus()
        consensus.Save(filename)

    def Consensus(self, profile):
        consensus = YDNA([])
        indexes = {
            0: 'A',
            1: 'C',
            2: 'G',
            3: 'T'
           }

        for col in range(profile.GetColCount()):
            max_index = 0
            max_count = 0
            for row in range(profile.GetRowCount()):
                if int(profile.GetItem(row, col)) > max_count:
                    max_count = int(profile.GetItem(row, col))
                    max_index = row
            consensus.Append(indexes[max_index])
        return consensus