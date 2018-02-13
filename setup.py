from setuptools import setup

setup(
  name = 'py_opc_n2_logger',
  version = '0.1.2',
  description = 'A Python data logging package for the Alphasense OPC-N2 particle sensor',
  url = 'http://github.com/skgrange/py_opc_n2_logger',
  author = 'Stuart K. Grange',
  author_email = 's.k.grange@gmail.com',
  license = 'MIT',
  packages = ['py_opc_n2_logger'],
  install_requires = ['py-opc', 'pandas'],
  scripts = ['bin/alphasense_opc_n2_logger'],
  zip_safe = True
)
