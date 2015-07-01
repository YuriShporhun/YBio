from YDNA import YDNA
from YSeq import YSeq

class YRNA(YSeq):

    def __init__(self, sequence):
        if type(sequence) == YDNA:
            sequence = self.__FromDNA(sequence)
        self._sequence = sequence[:]

    def __FromDNA(self, dna_sequence):
        return str(dna_sequence).replace('T', 'U') 