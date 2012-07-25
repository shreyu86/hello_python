#!/usr/bin/python
from pipes.lib.pipeline import Pipeline
import logging
import argparse
parser = argparse.ArgumentParser(description='Proccess String via a pipeline')
parser.add_argument("-s", action="store", dest="inputstring",
                    help="String to Be Proccessed", default="Hello Python")
parser.add_argument("-c", action="store", dest="configfile",
                    help="Configfile Containing Instructions",
                    default="config.yaml")
args = parser.parse_args()


def main():
    input = {}
    logging.basicConfig(level='INFO')
    input['original'] = args.inputstring
    pipeline = Pipeline(args.configfile)
    logging.info('Input is = {0}'.format(input))
    pipeline.run(input)
    logging.info('Input is now = {0}'.format(input))


if __name__ == "__main__":
    main()
