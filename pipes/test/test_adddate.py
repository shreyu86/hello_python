#!usr/bin/python
import unittest
import datetime
from pipes.steps.adddate import Step


class TestAddDateStep(unittest.TestCase):

    def setUp(self):
        self.procstringkey = 'original'
        self.stepkey = "DATE"

    def testmirror(self):
        input = {}
        inputstring = " hello "
        expectedoutput = datetime.datetime.now()
        expectedoutput = expectedoutput.strftime("%m-%d-%Y")
        input[self.procstringkey] = inputstring
        mirrorstep = Step()
        mirrorstep.run(input, self.procstringkey, self.stepkey)
        self.assertEqual(input[self.stepkey], expectedoutput)

    def tearDown(self):
        self.procstringkey = None
        self.stepkey = None
