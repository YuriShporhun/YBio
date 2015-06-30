from unittest import TestCase
from YSeq import YSeq

__author__ = 'Yuri Shporhun'

class TestYSeq(TestCase):
    def test_Count(self):
        #The test sequence has to have 3 A, 4 T, 5 C and 6 G
        test_sequence = "AAATTTTCCCCCGGGGGG"
        seq = YSeq(test_sequence)
        a_count = seq.Count("A")
        t_count = seq.Count("T")
        c_count = seq.Count("C")
        g_count = seq.Count("G")
        self.assertEqual(a_count, 3, "Actual A count is 3")
        self.assertEqual(t_count, 4, "Actual T count is 4")
        self.assertEqual(c_count, 5, "Actual C count is 5")
        self.assertEqual(g_count, 6, "Actual G count is 6")

    def test_Append(self):
        pass

    def test_Save(self):
        pass

    def test_Load(self):
       pass