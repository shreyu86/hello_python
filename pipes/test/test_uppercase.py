#!usr/bin/python
import unittest
from pipes.steps.uppercase import Step


class TestUpperCaseStep(unittest.TestCase):

    def setUp(self):
        self.procstringkey = 'original'
        self.stepkey = "UPPERCASE"

    def testuppercase(self):
        input = {}
        inputstring = "hello"
        input[self.procstringkey] = inputstring
        uppercasestep = Step()
        uppercasestep.run(input, self.procstringkey, self.stepkey)
        self.assertEqual(input[self.stepkey], inputstring.upper())

    def tearDown(self):
        self.procstringkey = None
        self.stepkey = None
