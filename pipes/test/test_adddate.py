#!usr/bin/python
from nose.tools import eq_
import datetime
from pipes.steps.adddate import Step
class testAddDateStep:
  procstringkey = 'original'
  stepkey = "DATE"
  def testmirror(self):
    input = {}
    inputstring = " hello "
    expectedoutput = datetime.datetime.now()
    expectedoutput = expectedoutput.strftime("%m-%d-%Y")
    input[self.procstringkey]=inputstring
    mirrorstep = Step()
    mirrorstep.run(input,self.procstringkey,self.stepkey)
    eq_(input[self.stepkey],expectedoutput)

