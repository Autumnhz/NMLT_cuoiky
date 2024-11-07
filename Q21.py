# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:46:02 2024

@author: LAPTOP
"""

from typing import List, Optional, Tuple
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    num_set = set()
    for n in nums:
        x = target - n
        if x in num_set:
            return (x, n)
        num_set.add(n)
    return None


if __name__=='__main__':
    print(question_21([1, 2, 3, 4, 5], 10))
