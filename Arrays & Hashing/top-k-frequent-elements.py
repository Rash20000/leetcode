"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
It is guaranteed that the answer is unique.

Hashtable
"""
from typing import List, Any


class Solution:
    def topKFrequent(self: Any, nums: List[int], k: int) -> List[int]:
        valuemap = {}
        for item in nums:
            valuemap[item] = valuemap.get(item, 0) + 1
        valuemap = sorted(valuemap.items(), key=lambda x: x[1], reverse=True)
        output = [x[0] for x in valuemap[:k]]
        return output


print(Solution.topKFrequent(None, nums=[23, 4, 4, 1, 1, 1, 1, 11, 1], k=2))
