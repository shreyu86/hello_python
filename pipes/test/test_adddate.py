#!usr/bin/python
import datetime
from pipes.steps.adddate import Step
procstringkey = 'original'
stepkey = "DATE"
def testmirror():
  input = {}
  inputstring = " hello "
  expectedoutput = datetime.datetime.now()
  expectedoutput = expectedoutput.strftime("%m-%d-%Y")
  input[procstringkey]=inputstring
  mirrorstep = Step()
  mirrorstep.run(input,procstringkey,stepkey)
  assert input[stepkey]==expectedoutput