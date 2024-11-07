# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:25:14 2024

@author: LAPTOP
"""

def question_24(nums: list[int]) -> int:
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1
        if count[i] > len(nums) // 2:
            return i
        

if __name__=='__main__':
    print(question_24([2, 2, 1, 1, 1, 2, 2]))