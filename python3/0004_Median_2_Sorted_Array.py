#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n----- | Leetcode 4. Median of Two Sorted Arrays. | =====\n')

nums1 = [1, 3, 9, 44, 786, 4853, 7654]
nums2 = [2, 564, 987, 2934, 4645]

nums3 = nums1 + nums2
nums3.sort()
lens3 = len(nums3)

rst = 0.0
if lens3 % 2 == 1:
    rst = nums3[lens3 // 2]
else:
    rst = (nums3[lens3 // 2] + nums3[lens3 // 2 - 1]) / 2.0

if int(rst) == 675:
    print(f'Result = {rst}. ----- Wunderbar! You got correct result.')
