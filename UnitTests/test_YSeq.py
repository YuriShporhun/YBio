from unittest import TestCase
from YSeq import YSeq

__author__ = 'Yuri Shporhun'

class TestYSeq(TestCase):

    def test___init__(self):
        pass
        #self.assertRaises(TypeError, YSeq(1))

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
        with open("TestData/YSeq/save/Input") as file:
            example = file.readline()

        seq = YSeq(example)
        seq.save("TestData/YSeq/save/Output", "+")

        with open("TestData/YSeq/save/ExpectedOutput") as file:
            expected_result = file.readline()

        with open("TestData/YSeq/save/Output") as file:
            result = file.readline()

        self.assertEqual(expected_result, result)

    def test_Load(self):
        pass