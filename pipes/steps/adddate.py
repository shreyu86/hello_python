import logging
import datetime


class Step(object):

    def run(self, input, procstringkey, stepkey):
        logging.info('Adding Date')
        now = datetime.datetime.now()
        now = now.strftime("%m-%d-%Y")
        input[stepkey] = now
