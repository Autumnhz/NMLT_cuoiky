# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:26:22 2024

@author: LAPTOP
"""

def question_18(s: str) -> str:
    s = s.strip()  
    s = ' '.join(s.split())
    return s


if __name__=='__main__':
    print(question_18("Python   is   fun"))