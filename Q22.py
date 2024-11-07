# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:07:12 2024

@author: LAPTOP
"""

def question_22(nums: list[int]) -> None:
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero] = nums[i]
            zero += 1
            
    for i in range(zero, len(nums)):
        nums[i] = 0
        
        
if __name__=='__main__':
    nums = [0, 0, 1]
    question_22(nums)
    print((nums))