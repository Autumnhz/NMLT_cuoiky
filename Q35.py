# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:07:21 2024

@author: LAPTOP
"""

def question_35(s: str) -> str:
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i+1,n):
            substring = s[i:j]
            if substring in s[j:] and len(substring) > len(longest):
                longest = substring
                
    return longest

if __name__=='__main__':
    print(question_35("aabcdeaabcd"))