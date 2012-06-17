#!usr/bin/python
from pipes.steps.uppercase import Step
procstringkey = 'original'
stepkey = "UPPERCASE"
def testuppercase():
  input = {}
  inputstring = "hello"
  input[procstringkey]=inputstring
  uppercasestep = Step()
  uppercasestep.run(input,procstringkey,stepkey)
  assert input[stepkey]==inputstring.upper()
