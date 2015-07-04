from unittest import TestCase
from YDNA import YDNA

__author__ = 'Yuri Shporhun'

class TestYDNA(TestCase):
    def test_append(self):
        dna = YDNA("ACGT")
        dna.append("A")
        self.assertEqual(str(dna), "ACGTA")

    def test_nucleotides_count(self):
        with open("TestData/YDNA/nucleotides_count/Input") as file:
            example = file.readline()
        dna = YDNA(example)
        count_of_nucleotides = dna.nucleotides_count()
        with open("TestData/YDNA/nucleotides_count/ExpectedOutput") as file:
            expected_output = file.readline()
        self.assertEqual(' '.join([str(x) for x in count_of_nucleotides]), expected_output)

    def test_complement(self):
        pass

    def test_reverse_complement(self):
        pass

    def test_entries_indexes(self):
        pass