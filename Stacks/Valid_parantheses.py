# https://leetcode.com/problems/valid-parentheses/description/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
open_lookup = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def is_open(bracket: str) -> bool:
    return True if bracket in open_lookup else False


class Solution:
    def isValid(self, s: str) -> bool:
        lifo_ds = []
        if not len(s) % 2 == 0:
            return False  # its not even. cant be a valid parenthesis. save compute

        for i in s:
            if is_open(i):
                lifo_ds.append(i)
            else:  # we got a closing parenthesis
                try:
                    last_open = lifo_ds.pop()
                except IndexError:
                    return False # cant pop from empty lifo
                else:
                    if open_lookup[last_open] != i:
                        return False

        return True if len(lifo_ds) == 0 else False




print(Solution().isValid("(]"))
