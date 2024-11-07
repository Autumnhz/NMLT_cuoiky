# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:34:21 2024

@author: LAPTOP
"""

def question_25(nums: list[int]) -> list[int]:
    bp = [x**2 for x in nums]
    bp.sort()
    return bp


if __name__=='__main__':
    print(question_25([-7, -3, 2, 3, 11]))