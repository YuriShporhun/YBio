from unittest import TestCase
from YSeq import YSeq

__author__ = 'Yuri Shporhun'

class TestYSeq(TestCase):

    def test_Count(self):
        #The test sequence has to have 3 A, 4 T, 5 C and 6 G
        test_sequence = "AAATTTTCCCCCGGGGGG"
        seq = YSeq(test_sequence)
        a_count = seq.count("A")
        t_count = seq.count("T")
        c_count = seq.count("C")
        g_count = seq.count("G")
        self.assertEqual(a_count, 3)
        self.assertEqual(t_count, 4)
        self.assertEqual(c_count, 5)
        self.assertEqual(g_count, 6)

    def test_Append(self):
        #The test sequence has to contain ATG
        test_sequence = "ATG"
        result_sequence = "ATGA"
        seq = YSeq(test_sequence)
        seq.append("A")
        self.assertEqual(str(seq), result_sequence)

    def test_Save(self):
        pass

    def test_Load(self):
        pass