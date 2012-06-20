#!usr/bin/python
import unittest
from pipes.steps.duplicate import Step


class TestDuplicateStep(unittest.TestCase):

    def setUp(self):
        self.procstringkey = 'original'
        self.stepkey = "DUPLICATE"
        self.dupsep = " "

    def testduplicate(self):
        input = {}
        inputstring = " hello "
        input[self.procstringkey] = inputstring
        expectedoutput = inputstring + self.dupsep + inputstring
        duplicatetest = Step()
        duplicatetest.run(input, self.procstringkey, self.stepkey)
        self.assertEqual(input[self.stepkey], expectedoutput)

    def tearDown(self):
        self.procstringkey = None
        self.stepkey = None
        self.dupsep = None
