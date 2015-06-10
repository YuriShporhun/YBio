from YSeq import YSeq
from YRules import YRules
from YConstants import YConstants

class YDNA(YSeq):
    '''This class represetnts a DNA sequence'''
    __list_of_nucleotides = ['A', 'T', 'C', 'G', '_']

    #Constructor makes a copy of DNA sequence
    def __init__(self, dna_sequence):
        self.__CheckDNAMistakes(dna_sequence)
        super().__init__(dna_sequence)

    def Append(self, symbol):
        self.__CheckDNAMistakes(symbol)
        super().Append(symbol)

    def NucleotidesCount(self):
        '''This method returns count of nucleotides as tuple
        nucleotide sequence: A C G T
        '''
        a_count = super().Count('A')
        c_count = super().Count('C')
        g_count = super().Count('G')
        t_count = super().Count('T')
        return (a_count, c_count, g_count, t_count)
            
    #This method checks the DNA sequence errors
    def __CheckDNAMistakes(self, dna_sequence):
        for nucleotide in dna_sequence:
            if nucleotide not in self.__list_of_nucleotides:
                raise ValueError(nucleotide)

    def Complement(self):
        complement = []
        [complement.append(YRules.complement_dna[x]) for x in self._sequence]
        return complement

    def ReverseComplement(self):
        return self.Complement()[::-1]

    def EntriesIndexes(self, sub_sequence, indexing = 'zero_based'):
        indexes = []
        dna = ''.join(self._sequence)
        start = 0
        while True:
            current_position = dna.find(str(sub_sequence), start)
            if current_position != -1:
                start = current_position + 1
                indexes.append(current_position + YConstants.indexing[indexing])
            else:
                break
        return indexes
