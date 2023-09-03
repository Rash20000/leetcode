# Hash Table
# String
# Sorting


class Solution:
    # s and t consist of lowercase English letters.

    def isAnagram(self, s: str, t: str) -> bool:
        lettersCount = dict()

        if len(s) != len(t):
            return False

        for char in s:
            lettersCount[char] = lettersCount.get(char, 0) + 1

        for char in t:
            count = lettersCount.get(char, 0)
            if count <= 0:
                return False
            lettersCount[char] = count - 1

        for val in lettersCount.values():
            if val != 0:
                return False

        return True
print(Solution().isAnagram("abc", "bac"))
