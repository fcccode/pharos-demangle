from setuptools import setup

#from distutils.core import setup
from distutils.extension import Extension

import os
import sys

###
# build an rpm with the command:
###
#
#  python3 setup.py bdist_rpm


__version__ = '1.1'

libraries = ['boost_python'] if sys.version_info[0] < 3 else ['boost_python3']
libraries += ['boost_system','boost_filesystem','boost_program_options']

pydemanglemodule = Extension("pydemangle",
                        define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '1')],
                        include_dirs = [os.path.join(os.getcwd(), 'libdemangle'), os.getcwd(),],
                        libraries = libraries,
                        library_dirs = [os.getcwd(),],
                        sources = ['libdemangle/codes.cpp', 'libdemangle/json.cpp', 'libdemangle/demangle_json.cpp', 'libdemangle/demangle.cpp', 'libdemangle/demangle_text.cpp', 'src/pydemanglemodule.cpp'],
                        extra_compile_args=["-std=c++11", "-Wall", "-Wextra", "-Wshadow", "-Wstrict-aliasing"],
                        language='c++11')

setup(name='pydemangle',
      version=__version__,
      include_package_data=True,
      description='Python interface for Pharos Demangler',
      url='https://code.cc.cert.org/Malicious-Code-Team/demangle',
      author='Garret Wassermann',
      author_email='gwassermann@cert.org',
      license='MIT',
      classifiers=['Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3'],
      ext_modules=[pydemanglemodule],
      zip_safe=False)
