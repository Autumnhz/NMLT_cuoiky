# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:44:27 2024

@author: LAPTOP
"""

from typing import Optional
def question_20() -> Optional[str]:
    gtri = input('Nhập giá trị: ')
    return gtri if gtri else None


if __name__=='__main__':
    print(question_20())
    