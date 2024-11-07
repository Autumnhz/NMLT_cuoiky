# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:12:46 2024

@author: LAPTOP
"""

def question_10() -> None:
    n = input('Nhập danh sách số nguyên(phân cách bằng khoảng trắng): ')
    ds = [int(i) for i in n.split()] if n else None
    return ds


if __name__ == '__main__':
    print(question_10())