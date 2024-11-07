# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:32:44 2024

@author: LAPTOP
"""

def question_38(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

if __name__=='__main__':
    print(question_38(2))
    print(question_38(3))
  