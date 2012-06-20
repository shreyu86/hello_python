import logging


class Step(object):

    def run(self, input, procstringkey, stepkey):
        logging.info('Calculating Length')
        stringOriginal = input[procstringkey]
        if stringOriginal is not None:
            input[stepkey] = len(stringOriginal)
        else:
            input[stepkey] = input[procstringkey]
