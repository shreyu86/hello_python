#!usr/bin/python
from pipes.steps.mirror import Step
procstringkey = 'original'
stepkey = "MIRRORING"
def testmirror():
  input = {}
  inputstring = " hello "
  input[procstringkey]=inputstring
  mirrorstep = Step()
  mirrorstep.run(input,procstringkey,stepkey)
  assert input[stepkey]==inputstring[::-1]