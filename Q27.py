# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:54:52 2024

@author: LAPTOP
"""

def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    char = strs[0]
    for string in strs[1:]:
        while string[:len(char)] != char:
            char = char[:-1]
            if not char:
                return ""
    
    return char


if __name__=='__main__':
    print(question_27(["flower", "flow", "flight"]))