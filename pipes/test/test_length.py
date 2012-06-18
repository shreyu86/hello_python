#!usr/bin/python
from nose.tools import eq_
from pipes.steps.length import Step
class testLengthStep:
  procstringkey = 'original'
  stepkey = "LENGTH"
  def testlength(self):
    input = {}
    inputstring = "hello"
    input[self.procstringkey]=inputstring
    lengthstep= Step()
    lengthstep.run(input,self.procstringkey,self.stepkey)
    eq_(input[self.stepkey],len(inputstring))
