import json
from typing import List


# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
#  If there is no common integer amongst nums1 and nums2, return -1.
# both arrays are sorted in ascending order.


class Solution:
    def getCommon_map(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = {x: True for x in nums2}

        for i in nums1:
            if nums2.get(i):
                return i
        return -1


with open('./nums1.json', 'r') as nums1:
    nums1 = json.load(nums1)
with open('./nums2.json', 'r') as nums2:
    nums2 = json.load(nums2)
print(Solution().getCommon_map(nums1, nums2))
