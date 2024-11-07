# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:26:34 2024

@author: LAPTOP
"""

def question_34(s: str) -> int:
     ds_char = []
     max_length = 0

     for char in s:
         while char in ds_char:
             ds_char.pop(0)  
         ds_char.append(char)
         max_length = max(max_length, len(ds_char))
    
     return max_length

if __name__ == '__main__':
    print(question_34("pwwkew"))
        
        