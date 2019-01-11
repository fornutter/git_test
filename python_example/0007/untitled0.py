# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:46:05 2019

@author: as us
"""

import re
c=re.compile(r'[aaa|bbb]')


i="aaabbb"
if i.startswith(c):
    print(123)
else:
    print(456)
