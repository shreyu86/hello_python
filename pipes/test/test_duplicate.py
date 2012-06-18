#!usr/bin/python
from nose.tools import eq_
from pipes.steps.duplicate import Step
class testDuplicateStep:
  procstringkey = 'original'
  stepkey = "DUPLICATE"
  dupsep = " "
  def testduplicate(self):
    input = {}
    inputstring = " hello "
    input[self.procstringkey]=inputstring
    expectedoutput = inputstring+self.dupsep+inputstring
    duplicatetest = Step()
    duplicatetest.run(input,self.procstringkey,self.stepkey)
    eq_(input[self.stepkey],expectedoutput)
