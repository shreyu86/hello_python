import sys
import importlib
import logging
import datetime
import yaml
import hashlib
### Edited this step to include an config file in YAML 
### which contains the string ID to be acted on and which pipelines to execute.

class Pipeline(object):

    #STEPS = ['steps.uppercase','steps.duplicate','steps.adddate']

    def __init__(self,filename):
        self.load_components(filename)

   
    def create_object(self, module, object_name, **kwargs):

        mod = importlib.import_module(module)

        if kwargs:
            obj = getattr(mod, object_name)(**kwargs)
        else:
            obj = getattr(mod, object_name)()

        return obj
        
    def load_components(self,filename):
        logging.info('Loading components')
        self.configfile = filename
        self.pipeline = []
        self.STEPS    = []
        self.configdict = {}
        self.procstring = None
        h = hashlib.new('ripemd160')
        try:
	  filehandler = open (self.configfile,'r')
	  yamlread = yaml.load(filehandler)
	  self.STEPS = yamlread['pipelinesteps']
	  self.procstring = yamlread['proc_string_id']
	except:
	  logging.exception("Cannot load the config file")
        logging.info('Config file loaded')
        for step in self.STEPS:
	    splitstep_id = step.split(',')
	    step_fullname = splitstep_id[0]
	    step_displayname = splitstep_id[1]
            logging.info('Initializing {0}'.format(step_fullname))
            try:
                step_object = self.create_object(step_fullname, 'Step')
                self.pipeline.append(getattr(step_object,'run'))
                h.update(str(getattr(step_object,'run')))
                self.configdict[h.hexdigest()]=step_displayname
            except:
                logging.warning('Error occured loading {0}'.format(step_fullname))
                logging.exception('Error loading pipeline component')
    def run(self, input):
        h = hashlib.new('ripemd160')
        #print self.configdict
        for component in self.pipeline:
            try:
	        #print "After "+str(component)
	        h.update(str(component))
	      ## Add the string on which the pipeline has to executed
                currentstep = self.configdict[h.hexdigest()]
                component(input,self.procstring,currentstep)
            except:
                logging.exception('Unable to run component')