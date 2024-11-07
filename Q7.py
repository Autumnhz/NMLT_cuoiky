# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:48:46 2024

@author: LAPTOP
"""

import random
def question_7(n: int) -> (float, float):
   ds =  [random.random() for _ in range(n)]
   sln = max(ds)
   snn = min(ds)
   return sln, snn


if __name__=='__main__':
   print(question_7(5))