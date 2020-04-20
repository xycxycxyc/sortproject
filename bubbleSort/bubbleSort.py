#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/20 15:17
# @Author: xuyongchuan
# @File  : bubbleSort.py.py


def bubbleSort(nums):
    haschange = True
    for i in range(1, len(nums)):
        haschange = False
        for j in range(len(nums)-i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                haschange = True
        if haschange is False:
            return nums
    return nums


if __name__ =='__main__':
    test_nums = [2, 3, 1, 7, 3, 4]
    test_nums = bubbleSort(test_nums)
    print(test_nums)



