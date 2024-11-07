# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:02:14 2024

@author: LAPTOP
"""

def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    else:
        return None
    
    
if __name__=='__main__':
    lst = [1,2,3,4,5]
    print(question_5(lst,3))
    lst = [10,20,30,40]
    print(question_5(lst,25))