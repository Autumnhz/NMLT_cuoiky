# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:22:29 2024

@author: LAPTOP
"""
import itertools

def question_36(nums: list[int]) -> list[list[int]]:
    s = itertools.permutations(nums)
    return list(map(list,s))


if __name__=='__main__':
    print(question_36([1,2,3]))
    print(question_36([0,1]))
    print(question_36([1]))
    
    