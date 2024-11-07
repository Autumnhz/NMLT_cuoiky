# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:58:41 2024

@author: LAPTOP
"""

import random 

def question_2(n: int) -> (int, float):
   
    ds = []
    for i in range(n):
        number = random.randint(1, 100) 
        ds.append(number) 

    tong = sum(ds)
    trungbinh = tong / n 
    return tong, trungbinh




if __name__=='__main__':
    print(question_2(5))  
    print(question_2(10))
    
