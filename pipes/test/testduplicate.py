#!usr/bin/python
from pipes.steps.duplicate import Step
procstringkey = 'original'
stepkey = "DUPLICATE"
dupsep = " "
def testduplicate():
  input = {}
  inputstring = " hello "
  input[procstringkey]=inputstring
  expectedoutput = inputstring+dupsep+inputstring
  duplicatetest = Step()
  duplicatetest.run(input,procstringkey,stepkey)
  assert input[stepkey]==expectedoutput