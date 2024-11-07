# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 01:01:52 2024

@author: LAPTOP
"""

def question_11(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return question_11(n-1) + question_11(n-2)
    
    
if __name__=='__main__':
   print(question_11(10))