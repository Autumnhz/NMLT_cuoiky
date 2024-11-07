# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:32:50 2024

@author: LAPTOP
"""

def question_37(s: str) -> bool:
    ds = []
    ky_tu = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in ['(', '{', '[']:
            ds.append(char)
        else:
            if not ds or ds.pop() != ky_tu [char]:
                return False

    return not ds

if __name__=='__main__':
    print(question_37("()"))
    print(question_37("()[]{}"))
    print(question_37("(]"))
    print(question_37("([)]"))
    print(question_37("{[]}"))

    