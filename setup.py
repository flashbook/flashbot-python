from setuptools import setup
from pypandoc import convert_file

print(setup.__module__)

setup(name='flashbot',
      description='Official Python client library for Flashbot',
      long_description=convert_file('README.md', 'md'),
      version='0.1.0.dev1',
      url='https://github.com/flashbook/flashbot-python',
      author='Alex Lopatin',
      author_email='alex@flashbook.io',
      license='Apache2',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=['flashbot'],
      install_requires=[
          'pytorch>=0.1.2',
          'pyro-ppl>=0.1.2'
      ])
