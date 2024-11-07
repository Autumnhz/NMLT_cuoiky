# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:22:30 2024

@author: LAPTOP
"""

def question_23(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__=='__main__':
    print(question_23([1, 2, 3, 4]))