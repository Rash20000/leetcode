# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        o = '('
        c = ')'

        stack = []
        results = []
        def rec(open_count, close_count)->str:

            if open_count == close_count == n:
                results.append(''.join(stack))
                return

            if open_count < n:
                stack.append(o)
                rec(open_count+1, close_count)
                stack.pop()
            if close_count < open_count:
                stack.append(c)
                rec(open_count, close_count+1)
                stack.pop()
        rec(0,0)
        return results

print(Solution().generateParenthesis(2))