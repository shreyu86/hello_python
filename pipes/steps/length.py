﻿import logging
class Step(object):
###Modified to include the proccess string key so that original need not be hardcoded
    def run(self, input, procstringkey, stepkey):
        logging.info('Calculating Length')
        stringOriginal  = input[procstringkey]
        if stringOriginal is not None:
	  input[stepkey] = len(stringOriginal)
        else:
	  input[stepkey] = input[procstringkey]
	  ##Basically nothing is returned
        
