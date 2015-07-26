#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from YSeq import YSeq
from YRules import YRules
from YConstants import YConstants

class YDNA(YSeq):
    """
    En: This class represents a DNA sequence
    Ru: Данный класс инкапсулирует последовательность ДНК
    """

    __list_of_nucleotides = ['A', 'T', 'C', 'G', '_']

    def __init__(self, dna_sequence):
        self.__check_dna_mistakes(dna_sequence)
        super.__init__(dna_sequence)

    def append(self, symbol):
        self.__check_dna_mistakes(symbol)
        super.append(symbol)

    def nucleotides_count(self):
        """
        En: This method returns count of nucleotides as tuple
        Ru: Данный метод возвращает количество нуклеотидов A C G и T в виде кортежа
        :return: Tuple that contains the count of A C G and T: (A, C, G, T)
        """
        a_count = super.count('A')
        c_count = super.count('C')
        g_count = super.count('G')
        t_count = super.count('T')
        return a_count, c_count, g_count, t_count

    def __check_dna_mistakes(self, dna_sequence):
        """
        En: This method checks the DNA sequence errors
        :param dna_sequence: custom DNA sequence
        """
        for nucleotide in dna_sequence:
            if nucleotide not in self.__list_of_nucleotides:
                raise ValueError(nucleotide)

    def complement(self):
        """

        :return:
        """
        complement = []
        [complement.append(YRules.complement_dna[x]) for x in self._sequence]
        return complement

    def reverse_complement(self):
        """

        :return:
        """
        return self.Complement()[::-1]

    def entries_indexes(self, sub_sequence, indexing='zero_based'):
        """

        :param sub_sequence:
        :param indexing:
        :return:
        """
        indexes = []
        dna_sequence = ''.join(self._sequence)
        start = 0
        while True:
            current_position = dna_sequence.find(str(sub_sequence), start)
            if current_position != -1:
                start = current_position + 1
                indexes.append(current_position + YConstants.indexing[indexing])
            else:
                break
        return indexes