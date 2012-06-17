import os
from pipes.lib.pipeline import Pipeline
import logging
from flask import Flask
app = Flask(__name__)

def runpipeline(inputstring):
  input = {}
  logging.basicConfig(level='INFO')
  input['original'] = inputstring
  pipeline = Pipeline('config.yaml')
  logging.info('Input is = {0}'.format(input))
  pipeline.run(input)
  logging.info('Input is now = {0}'.format(input))
  return str(input)
@app.route('/')
def app_default():
  return runpipeline('Hello Python')
@app.route('/<customstring>')
def app_userstring(customstring):
  if customstring is not None:
    return runpipeline(customstring)
  else:
    return runpipeline('Hello World')
if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
