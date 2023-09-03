from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for num in nums:
            if num not in values:
                values.add(num)
            else:
                return True
        return False


def unit_test():
    print(Solution().containsDuplicate([1, 2, 3, 1]), True)
    print(Solution().containsDuplicate([1, 2, 3, 4]), False)
unit_test()