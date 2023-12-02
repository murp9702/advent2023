import unittest
import sys
sys.path.append("..")
from day1.day1 import *

sampleText = [line.rstrip() for line in open("sampleInput.txt")]
sampleTextPt2 = [line.rstrip() for line in open("sampleInputPt2.txt")]

class Day1Test(unittest.TestCase):
    def test_Parsing(self):
        correctValues = (12,38,15,77)
        for x in range(len(stripNumbers(sampleText))):
            self.assertEqual(stripNumbers(sampleText)[x], correctValues[x])
    def test_Addition(self):
        numbers = stripNumbers(sampleText)
        self.assertEqual(add(numbers), 142)
    def test_parsing_part2(self):
        correctValues = (29,83,13,24,42,14,76)
        parsedLines = lineParser(sampleTextPt2)
        for x in range(len(parsedLines)):
            self.assertEqual(stripNumbers(parsedLines)[x], correctValues[x])
        

if __name__ == "__main__":
    unittest.main()