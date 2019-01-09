# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:37:48 2019

@author: as us
"""
import re
a='''marry me, 
     please nut'''

b=re.split(r'[\s\,\n]+',a)
print(b)
