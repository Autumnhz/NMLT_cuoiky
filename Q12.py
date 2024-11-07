# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:43:53 2024

@author: LAPTOP
"""

import random
def question_12() -> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


if __name__=='__main__':
    n = random.randint(1,1000)
    print(n)
    print(question_12())
    