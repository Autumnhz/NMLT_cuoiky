# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:25:51 2024

@author: LAPTOP
"""

def question_3(s: str) -> (int, int):
    h = 0
    t = 0
    for k in s:
        if k.isupper():
            h += 1
        elif k.islower():
            t += 1
    return h, t
        

if __name__=='__main__':
    print(question_3("Python Programming"))
    
        
        