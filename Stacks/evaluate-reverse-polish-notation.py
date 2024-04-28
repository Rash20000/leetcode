# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
from typing import List
from collections import deque
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return int(a / b)


operands = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


class Solution:
    def __init__(self):
        self.number_stack = deque()

    def evalRPN(self, tokens: List[str]) -> int:
        for i in tokens:
            if i in operands:
                b, a = self.number_stack.popleft(), self.number_stack.popleft()
                c = operands[i](a,b)
                self.number_stack.appendleft(c)
            else:
                self.number_stack.appendleft(int(i))

        return self.number_stack[0]


print(Solution().evalRPN(["4","13","5","/","+"]))