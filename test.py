# -*- coding:utf-8 -*-
__author__ = "leo"

import os

a = os.path.abspath(__file__)
HERE = os.path.dirname(os.path.abspath(__file__))
HERE = os.path.join(HERE, '../')
b = os.getcwd()
print(a)
print(HERE)
print(b)