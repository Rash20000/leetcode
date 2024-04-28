# https://leetcode.com/problems/3sum/

class Solution:
    TARGET = 0

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tripplets = set[set]()
        # len nums is 3 at minimum
        start, index_skip_left_end, index_right_end = 0, len(tripplets) - 1
        while index_skip_left_end < index_right_end:
            start
        for index, value in enumerate(nums):

            left_end = nums[index + 1]
            right_end = nums[index_right_end]

            if index + left_end + right_end == Solution.TARGET:
                tripplets.add({index, index_skip_left_end, index_right_end})
            elif
