import logging


class Step(object):

    def run(self, input, procstringkey, stepkey):
        logging.info('Converting to uppercase')
        stringOriginal = input[procstringkey]
        if stringOriginal is not None:
            input[stepkey] = stringOriginal.upper()
        else:
            input[stepkey] = input[procstringkey]
