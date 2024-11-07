# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:28:51 2024

@author: LAPTOP
"""

from collections import Counter
from typing import Dict
def question_30(paragraph: str) -> Dict[str, int]:
    w = paragraph.split()
    w_dem = Counter(w)
    return dict(w_dem)


if __name__=='__main__':
    print(question_30("hello world hello"))