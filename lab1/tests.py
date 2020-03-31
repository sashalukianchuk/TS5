from testing_class import Testing
import unittest


class equivalenceClassTests(unittest.TestCase):

    MINVALUE = 0.606
    MAXVALUE = 120.829

    def test_moreThanRangeTM1(self):
        self.assertRaises(ValueError, Testing().pattern1, self.MAXVALUE+1)


    def test_lessThanRangeTM1(self):
        self.assertRaises(ValueError, Testing().pattern1, self.MINVALUE-1)


    def test_inRangeTM1(self):
        self.assertEqual(787267454.7512325, Testing().pattern1(self.MAXVALUE - self.MINVALUE))

    def test_moreThanRangeTM2(self):
        self.assertRaises(ValueError, Testing().pattern2, self.MAXVALUE+1)


    def test_lessThanRangeTM2(self):
        self.assertRaises(ValueError, Testing().pattern2, self.MINVALUE-1)


    def test_inRangeTM2(self):
        self.assertEqual(5808320.100638697, Testing().pattern2(self.MAXVALUE - self.MINVALUE))

    def test_moreThanRangeTM3(self):
        self.assertRaises(ValueError, Testing().pattern3, self.MAXVALUE+1)


    def test_lessThanRangeTM3(self):
        self.assertRaises(ValueError, Testing().pattern3, self.MINVALUE-1)


    def test_inRangeTM3(self):
        self.assertEqual(21123.943674489, Testing().pattern3(self.MAXVALUE - self.MINVALUE))

    def test_moreThanRangeTM4(self):
        self.assertRaises(ValueError, Testing().pattern4, self.MAXVALUE+1)


    def test_lessThanRangeTM4(self):
        self.assertRaises(ValueError, Testing().pattern4, self.MINVALUE-1)


    def test_inRangeTM4(self):
        self.assertEqual(765.099172, Testing().pattern4(self.MAXVALUE - self.MINVALUE))

    def test_NotADigitTM1(self):
        self.assertRaises(ValueError, Testing().pattern1, "qwerty")

    def test_NotADigitTM2(self):
        self.assertRaises(ValueError, Testing().pattern2, "qwerty")

    def test_NotADigitTM3(self):
        self.assertRaises(ValueError, Testing().pattern3, "qwerty")

    def test_NotADigitTM4(self):
        self.assertRaises(ValueError, Testing().pattern4, "qwerty")



class BoundaryValueClassTests(unittest.TestCase):

    MINVALUE = 0.606
    MAXVALUE = 120.829

    def test_moreThanRangeTM1(self):
        self.assertRaises(ValueError, Testing().pattern1, self.MAXVALUE + 0.001)

    def test_lessThanRangeTM1(self):
        self.assertRaises(ValueError, Testing().pattern1, self.MINVALUE - 0.001)

    def test_inMinRangeTM1(self):
        self.assertEqual(1.8659939892119992, Testing().pattern1(self.MINVALUE))

    def test_inMaxRangeTM1(self):
        self.assertEqual(803241758.945265, Testing().pattern1(self.MAXVALUE))

    def test_moreThanRangeTM2(self):
        self.assertRaises(ValueError, Testing().pattern2, self.MAXVALUE + 0.001)

    def test_lessThanRangeTM2(self):
        self.assertRaises(ValueError, Testing().pattern2, self.MINVALUE - 0.001)

    def test_inMinRangeTM2(self):
        self.assertEqual(2.8093974079199997, Testing().pattern2(self.MINVALUE))

    def test_inMaxRangeTM2(self):
        self.assertEqual(5896835.2867310215, Testing().pattern2(self.MAXVALUE))

    def test_moreThanRangeTM3(self):
        self.assertRaises(ValueError, Testing().pattern3, self.MAXVALUE + 0.001)

    def test_lessThanRangeTM3(self):
        self.assertRaises(ValueError, Testing().pattern3, self.MINVALUE - 0.001)

    def test_inMinRangeTM3(self):
        self.assertEqual(2.022977076, Testing().pattern3(self.MINVALUE))

    def test_inMaxRangeTM3(self):
        self.assertEqual(21335.935159281, Testing().pattern3(self.MAXVALUE))

    def test_moreThanRangeTM4(self):
        self.assertRaises(ValueError, Testing().pattern4, self.MAXVALUE + 0.001)

    def test_lessThanRangeTM4(self):
        self.assertRaises(ValueError, Testing().pattern4, self.MINVALUE - 0.001)

    def test_inMinRangeTM4(self):
        self.assertEqual(3.856584, Testing().pattern4(self.MINVALUE))

    def test_inMaxRangeTM4(self):
        self.assertEqual(768.955756, Testing().pattern4(self.MAXVALUE))



if __name__ == '__main__':
    unittest.main()
