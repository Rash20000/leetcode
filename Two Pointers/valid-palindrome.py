# https://leetcode.com/problems/valid-palindrome/
# https://leetcode.com/problems/valid-palindrome/submissions/1097932406/
class Solution:
    chars = ()
    def isPalindrome(self, s: str) -> bool:
        def ignore_char(char:str) -> bool:
            return char.isalnum() == False or char == ' '

        start = 0
        end = len(s) - 1

        if end <= 0:
            return True  # empty string



        while start <= end:
            beginning_char = s[start].lower()
            end_char = s[end].lower()

            if ignore_char(beginning_char):
                start = start + 1
                continue
            if ignore_char(end_char):
                end = end - 1
                continue

            if beginning_char != end_char:
                return False

            else:
                start += 1
                end -= 1

        return True

        # cheese way lol
        # return input == input[:-1]


print(Solution().isPalindrome("race a car"))
