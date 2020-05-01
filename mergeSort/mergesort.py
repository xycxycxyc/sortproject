#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/30 18:22
# @Author: xuyongchuan
# @File  : mergesort.py


def merge_sort(nums):
    if len(nums)<2:
        return nums
    middle = len(nums)//2
    left, right = nums[0:middle], nums[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__=='__main__':
    test_nums = [7, 6, 5, 6, 3, 9, 3]
    print(merge_sort(test_nums))
