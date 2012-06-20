import logging


class Step(object):

    def run(self, input, procstringkey, stepkey):
        logging.info('Duplicating')
        duplicationsep = " "
        stringOriginal = input[procstringkey]
        if stringOriginal is not None:
            input[stepkey] = stringOriginal + duplicationsep + stringOriginal
        else:
            input[stepkey] = input[procstringkey]
            #nothing is returned
