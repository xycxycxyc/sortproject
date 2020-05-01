#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/1 15:04
# @Author: xuyongchuan
# @File  : quicksort.py


def quick_sort(nums, left, right):
    if left < right:
        p = partition(nums, left, right)
        quick_sort(nums, left, p-1)
        quick_sort(nums, p+1, right)
        return nums


def partition(nums, left, right):
    pivot = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i+1], nums[j] = nums[j], nums[i+1]
            i += 1
    nums[i+1], nums[right] = nums[right], nums[i+1]
    return i+1


if __name__ == '__main__':
    test_nums = [7, 6, 5, 6, 3, 9, 3]
    print(quick_sort(test_nums, 0, len(test_nums)-1))