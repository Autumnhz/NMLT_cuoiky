# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:22:40 2024

@author: LAPTOP
"""

def question_33(nums: list[int]) -> tuple[int, int]:
  nums.sort()
  if len(nums) < 5:
    return None
  return nums[-2], nums[4]


if __name__ == '__main__':
  print(question_33([1, 3, 2, 5]))