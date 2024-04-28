# https://leetcode.com/problems/min-stack/submissions/1244038867/
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function
class MinStack:


    def __init__(self):

        self.all_values = list()
        self.minimum_value_stack = list()

    def push(self, val: int) -> None:
        if len(self.minimum_value_stack) == 0:
            self.minimum_value_stack.insert(0, val)


        elif self.minimum_value_stack[0] >= val:
            self.minimum_value_stack.insert(0, val)

        self.all_values.insert(0, val)

    def pop(self) -> None:
        value_to_pop = self.all_values.pop(0)
        if self.minimum_value_stack[0] == value_to_pop:
            self.minimum_value_stack.pop(0)

    def top(self) -> int:
        return self.all_values[0]

    def getMin(self) -> int:
        return self.minimum_value_stack[0]
