# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:21:35 2024

@author: LAPTOP
"""

import random
def question_17(n: int) -> list:
    ds = [random.randint(1,100) for _ in range(n)]
    ds.sort(reverse = True)
    return ds


if __name__=='__main__':
   print(question_17(3))