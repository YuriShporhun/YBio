from YSeq import YSeq
from YLoader import YLoader
from YDNA import YDNA
from YRNA import YRNA

class YSeqFunc:

    def __init__(self):
        pass

    @staticmethod
    def hamming_distance(seq_one, seq_two):
        """
        En: A Static method which calculates the Hamming distance
        between two sequences for
        """
        distance = 0
        for i in range(0, len(seq_one)):
            if seq_one[i] != seq_two[i]:
                distance += 1
        return distance

    @staticmethod
    def transition_transversion_ratio(seq_one, seq_two):
        """
        En: A Static method which calculates the Transiton and
        Transversion ratio
        """
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

class _YServiceMatrix:
    _matrix = []
    _cols = 0
    _rows = 0

    def __init__(self, dna_sequences):
        self._matrix = dna_sequences[:]
        self._cols = self.__normalize()
        self._rows = len(self._matrix)

    def __normalize(self):
        max_size = 0
        for seq in range(len(self._matrix)):
            if len(self._matrix[seq]) > max_size:
                max_size = len(self._matrix[seq])

        for seq in range(len(self._matrix)):
            if len(self._matrix[seq]) < max_size:
                self._matrix[seq] += ('_' * (max_size - len(self._matrix[seq])))
        return max_size

    def _transpose(self):
        self._matrix = [[self._matrix[j][i] for j in range(len(self._matrix))] for i in range(len(self._matrix[0]))]
        self._cols, self._rows = self._rows, self._cols

    def append(self, sequence):
        self._matrix.append(sequence)
        self._cols = self.__normalize()
        self._rows += 1

    def get_col_count(self):
        return self._cols

    def get_row_count(self):
        return self._rows

    def get_item(self, row, col):
        return self._matrix[row][col]

class YMatrix(_YServiceMatrix):
    def __init__(self, dna_sequences):
        super.__init__(dna_sequences)

    def __repr__(self):
        result = ''
        for item in self._matrix:
            result += str(item) + '\n'
        return result

    def profile(self):
        profile = YMatrix([])

        for col in range(self._cols):
            temp_dna = YDNA([])
            for row in range(self._rows):
                temp_dna.Append(self._matrix[row][col])
            profile.Append(temp_dna.Count())
            
        profile._transpose()
        return profile

    def save_profile(self, filename, designations = False):
        indexes = {
            0: 'A',
            1: 'C',
            2: 'G',
            3: 'T'
           }
        profile = self.Profile()
        profile._transpose()
        sign_flag = True
        with open(filename, 'w') as file:
            for i in range(profile.GetColCount()):
                if designations and sign_flag:
                    file.write(indexes[i] + ': ')
                for j in range(profile.GetRowCount()):
                    file.write(str(profile.GetItem(j, i)) + ' ')
                file.write('\n')

    def save_consensus(self, filename):
        consensus = self.Consensus()
        consensus.Save(filename)

    @staticmethod
    def consensus(profile):
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
