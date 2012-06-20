#!usr/bin/python
import unittest
from pipes.steps.length import Step


class TestLengthStep(unittest.TestCase):

    def setUp(self):
        self.procstringkey = 'original'
        self.stepkey = "LENGTH"

    def testlength(self):
        input = {}
        inputstring = "hello"
        input[self.procstringkey] = inputstring
        lengthstep = Step()
        lengthstep.run(input, self.procstringkey, self.stepkey)
        self.assertEqual(input[self.stepkey], len(inputstring))

    def tearDown(self):
        self.procstringkey = None
        self.stepkey = None
