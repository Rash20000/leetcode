"""
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
import concurrent
from concurrent.futures import ThreadPoolExecutor
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def group_anagram(values: list[str]):
            """
            will get all strings of equal values
            """
            sortedStringMap = {}
            for key in values:
                sortkey = ''.join(sorted(key))
                if sortkey not in sortedStringMap.keys():
                    sortedStringMap[sortkey] = [key]
                else:
                    sortedStringMap[sortkey].append(key)  # Use append without assignment

            return list(sortedStringMap.values())

        lengthStr = {}
        for s in strs:
            ls = len(s)
            if ls not in lengthStr:
                lengthStr[ls] = [s]
            else:
                lengthStr[ls] = lengthStr[ls] + [s]
        results = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(group_anagram, lengthStr[x]): x for x in lengthStr.keys()}
        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())
        return results

# print(Solution().group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(Solution().is_anagram("ear", "aea"))
