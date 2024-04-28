# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.


# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        def binary_search(value: int, elements: list):
            if len(elements) > 1:
                mid_index = int(len(elements) / 2)
                left_elements = elements[:mid_index]
                right_elements = elements[mid_index:]

                if value == elements[mid_index]:
                    return mid_index

                elif value < elements[mid_index]:
                    index_in_sub_array = binary_search(value, left_elements)
                    return index_in_sub_array

                elif value > elements[mid_index]:
                    index_in_sub_array = binary_search(value, right_elements)
                    if index_in_sub_array:
                        return len(left_elements) + index_in_sub_array

            elif elements[0] == value:
                return 0

            return False

        duplicate_sums_to_skip = set()  # We iterated over this and we dont have a pair for this
        for index, value in enumerate(numbers):
            if value in duplicate_sums_to_skip:
                continue
            compliment = target - value
            remaining_numbers = numbers[index:]
            current_index = index + 1
            compliment_index = binary_search(compliment, remaining_numbers)
            if compliment_index:
                searched_index = index + compliment_index + 1
                return [current_index, searched_index]

            else:
                # target for this is not present
                duplicate_sums_to_skip.add(value)
                continue


array = [1, 3, 4, 4]
target = 8
print(Solution().twoSum(array, target))
