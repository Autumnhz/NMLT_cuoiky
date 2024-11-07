# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:23:09 2024

@author: LAPTOP
"""

def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__=='__main__':
   print(question_1(2))
   print(question_1(1))