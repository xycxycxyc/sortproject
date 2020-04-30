#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/20 22:40
# @Author: xuyongchuan
# @File  : insertSort.py


def insertionsort(nums):
    for i in range(0, len(nums)):
        current = nums[i]
        while i-1 >= 0 and nums[i-1] > current:
            nums[i] = nums[i-1]
            i-=1
        nums[i] = current
    return nums


if __name__ == '__main__':
    test_nums = [7, 6, 5, 6, 3, 9, 3]
    test_nums = insertionsort(test_nums)
    print(test_nums)

