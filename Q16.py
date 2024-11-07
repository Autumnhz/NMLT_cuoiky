# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:03:59 2024

@author: LAPTOP
"""

def question_16(*arg) -> float:
    if not arg:
       return None
    return sum(arg)/len(arg) 


if __name__=='__main__':
   print(question_16(1,2,3,4,5))