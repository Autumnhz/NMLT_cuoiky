# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:55:27 2024

@author: LAPTOP
"""

import re
def question_9(s: str) -> bool:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]','',s)
    return s == s[::-1]


if __name__=='__main__':
    print(question_9("race a car"))
    