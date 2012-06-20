#!usr/bin/python
import unittest
from pipes.steps.mirror import Step


class TestMirrorStep(unittest.TestCase):

    def setUp(self):
        self.procstringkey = 'original'
        self.stepkey = "MIRRORING"

    def testmirror(self):
        input = {}
        inputstring = " hello "
        input[self.procstringkey] = inputstring
        mirrorstep = Step()
        mirrorstep.run(input, self.procstringkey, self.stepkey)
        self.assertEqual(input[self.stepkey], inputstring[::-1])

    def tearDown(self):
        self.procstringkey = None
        self.stepkey = None
