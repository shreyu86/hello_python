#!usr/bin/python
from nose.tools import eq_
from pipes.steps.mirror import Step
class testMirrorStep:
  procstringkey = 'original'
  stepkey = "MIRRORING"
  def testmirror(self):
    input = {}
    inputstring = " hello "
    input[self.procstringkey]=inputstring
    mirrorstep = Step()
    mirrorstep.run(input,self.procstringkey,self.stepkey)
    eq_(input[self.stepkey],inputstring[::-1])
