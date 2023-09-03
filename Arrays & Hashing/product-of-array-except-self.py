"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = []
        prefix_list = []
        suffix_list = []
        for i in range(0, len(nums)):
            try:
                prefix_list.append(prefix_list[i - 1] * nums[i])
            except IndexError:
                prefix_list.append(1 * nums[i])
        print(f"{prefix_list=}")

        reverse_nums = nums[::-1]
        for i in range(len(reverse_nums)):
            try:
                suffix_list.insert(i, suffix_list[i-1] * reverse_nums[i])
            except IndexError:
                suffix_list.insert(i, 1*reverse_nums[i])
        suffix_list = suffix_list[::-1]
        print(f"{suffix_list=}")


        for i in range(len(nums)):

            if i!=0:
                prefix = prefix_list[i-1]
            else:
                prefix = 1

            try:
                suffix = suffix_list[i+1]
            except IndexError:
                suffix = 1
            output_list.insert(i, prefix*suffix)

        return output_list



print(Solution.productExceptSelf(None, [1, 2, 3, 4]), [24, 12, 8, 6])
