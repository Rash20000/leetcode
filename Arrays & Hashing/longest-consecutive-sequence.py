class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        element_count = dict()




        max_length = 0  # since this is sorted, first element will be the smallest
        current_length = 0
        for index, item in enumerate(sorted_number_keys):
            if current_length == 0:
                current_length += 1
            if item + 1 in element_count:
                current_length += 1
            else:
                max_length = current_length if max_length < current_length else max_length
                current_length = 0

        return max_length


print(Solution.longestConsecutive(None, [-1, 0, 1, 3, 4, 5, 6, 7, 8, 9]))
