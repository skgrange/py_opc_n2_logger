from setuptools import setup

setup(
  name = "py_opc_n2_logger",
  version = "0.0.4",
  description = "A data logging programme for the Alphasense OPC-N2 particle sensor",
  url = "http://github.com/skgrange/py_opc_n2_logger",
  author = "Stuart K. Grange",
  author_email = "",
  license = "MIT",
  packages = ["py_opc_n2_logger"],
  install_requires = ["py-opc"],
  scripts = ["bin/alphasense_opc_n2_logger"],
  zip_safe = False
)
