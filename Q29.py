# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:27:39 2024

@author: LAPTOP
"""

from typing import List
def question_29(nums: List[int]) -> float:
    nums.sort()
    n = len(nums)
    if n%2 == 1:
        trungvi = nums[n//2]
    else:
        trungvi = (nums[n//2 - 1] + nums[n//2]) / 2
        
    return trungvi


if __name__=='__main__':
    print(question_29([1, 2, 3, 4]))