#!/usr/bin/python

from setuptools import setup
setup(name='PipeProject',
      version='0.1',
      description='Pipes for plumbing at Shopply',
      author='Shreyas Karnik',
      author_email='shreyu86@gmail.com',
      url = 'https://github.com/shreyu86/hello_python/',
      packages=['pipes', 'pipes.lib', 'pipes.steps','pipes.test'],
      package_data = { '' : ['*.yaml'] },
      provides = ['pyYAML','datetime','hashlib'],
      )
