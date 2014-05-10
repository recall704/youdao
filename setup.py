#encoding:utf-8
from setuptools import setup,find_packages
import sys,os

version = '0.1'

setup(name='yd',
      version=version,
      description="有道词典终端版",
      long_description="""有道词典终端版""",
      keywords='python youdao dictionary',
      author='recall704',
      author_email='tk657309822@gmail.com',
      url='http://www.cnblogs.com/tk091',
      license='LGPL',
      scripts=["yd/yd.py"],
      entry_points={
        'console_scripts':[
			'yd = yd:main'
        ]
      },
)
