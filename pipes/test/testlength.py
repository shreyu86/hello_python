#!usr/bin/python
from pipes.steps.length import Step
procstringkey = 'original'
stepkey = "LENGTH"
def testlength():
  input = {}
  inputstring = "hello"
  input[procstringkey]=inputstring
  lengthstep= Step()
  lengthstep.run(input,procstringkey,stepkey)
  assert input[stepkey]==len(inputstring)
