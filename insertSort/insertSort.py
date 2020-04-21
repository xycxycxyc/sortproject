#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/20 22:40
# @Author: xuyongchuan
# @File  : insertSort.py.py

def insertionSort(nums):
    for i in range(0, len(nums)-1):
        current = nums[i]
        while i-1 >= 0 and nums[i-1] > current:
            nums[i] = nums[i-1]
            i-=1
        nums[i] = current
    return nums


if __name__ == '__main__':
    test_nums = [7, 6, 5, 6, 3, 3, 9]
    test_nums = insertionSort(test_nums)
    print(test_nums)

