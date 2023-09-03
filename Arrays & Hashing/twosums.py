class Solution(object):
    def twoSum(self, nums: list[int], target: int):
        valueIndexMap = {}
        for currentIndex, value in enumerate(nums):

            complement = target - value

            if complement in valueIndexMap:
                return [valueIndexMap[complement], currentIndex]
            else:
                valueIndexMap[value] = currentIndex

        return []


#

def unit_test():
    test = Solution().twoSum
    print(test([2, 7, 11, 15], 9))  # [0,1]
    print(test([3, 2, 4], 6))  # [1,2]
    print(test([3, 3], 6))  # [0,1]
    print(test([3, 3], 0))  # []


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
