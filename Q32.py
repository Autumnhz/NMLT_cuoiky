# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:47:46 2024

@author: LAPTOP
"""

from typing import List, Tuple
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    sc = [so for so in nums if so%2 == 0]
    sl = [so for so in nums if so%2 != 0]
    
    sc.sort(reverse=True)
    sl.sort()
    
    return sc, sl


if __name__=='__main__':
    print(question_32([4, 1, 3, 2, 7, 8, 5]))