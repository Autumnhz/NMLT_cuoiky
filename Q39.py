# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:41:46 2024

@author: LAPTOP
"""

def question_39(prices: list[int]) -> int:
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0

    for i in prices:
        if i < min_price:
            min_price = i
        profit = i - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit

if __name__=='__main__':
    print(question_39([6, 7, 8, 9, 20, 5]))
    print(question_39([7, 1, 5, 3, 6, 4]))
    print(question_39([7, 6, 4, 3, 1]))