# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:55:33 2024

@author: LAPTOP
"""

def question_13(s: str) -> int:
    w = s.split()
    return len(w)


if __name__=='__main__':
    print(question_13(" This is a test. "))