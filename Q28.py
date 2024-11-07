# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:05:54 2024

@author: LAPTOP
"""

from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count


if __name__=='__main__':
    print(question_28("hello"))
    