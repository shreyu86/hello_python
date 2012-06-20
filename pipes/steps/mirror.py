import logging


class Step(object):

    def run(self, input, procstringkey, stepkey):
        logging.info('Mirroring (Reversing)')
        stringOriginal = input[procstringkey]
        if stringOriginal is not None:
            input[stepkey] = stringOriginal[::-1]
        else:
            input[stepkey] = input[procstringkey]
