# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:20:39 2024

@author: LAPTOP
"""

def question_6(n: int) -> int:
    giaithua = 1
    for i in range(1, n+1):
        giaithua *=i 
    return giaithua

if __name__=='__main__':
    print(question_6(5))