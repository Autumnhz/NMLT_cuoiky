# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:26:33 2024

@author: LAPTOP
"""

from typing import List
from collections import Counter
def question_31(paragraph: str, n: int) -> List[str]:
    w_tach = paragraph.split()
    w_dem_xh = Counter(w_tach)
    w_dem_tong = len(w_tach)
    
    ds_w = []
    for word, count in w_dem_xh.items():
        if count / w_dem_tong > 0.2:
            ds_w.append(word)
    
    return ds_w

if __name__=="__main__":
    print(question_31("apple apple banana orange orange apple",2))
    
    