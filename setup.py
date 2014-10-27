#encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='yd',
      version=version,
      description="Linux Windows下通用的有道词典",
      long_description="""方便在terminal查询生词的小工具""",
      classifiers=[],
      keywords='python youdao dictionary terminal',
      author='recall',
      author_email='tk657309822@gmail.com',
      url='https://github.com/recall704',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points={
        'console_scripts':[
            'yd = yd.yd:main'
        ]
      },
)
