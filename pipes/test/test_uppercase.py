#!usr/bin/python
from nose.tools import eq_
from pipes.steps.uppercase import Step
class testUpperCaseStep:
  procstringkey = 'original'
  stepkey = "UPPERCASE"
  def testuppercase(self):
    input = {}
    inputstring = "hello"
    input[self.procstringkey]=inputstring
    uppercasestep = Step()
    uppercasestep.run(input,self.procstringkey,self.stepkey)
    eq_(input[self.stepkey],inputstring.upper())
