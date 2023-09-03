# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def convertLinkedListToList(self, l1):
        # this will save 1 compute to reverse
        value = []
        while l1:
            value.append(l1.val)
            l1 = l1.next
        return value

    def convertListToLinkedList(self, l1):
        # this will save 1 compute to re-reverse
        value = ListNode()
        current = value
        while l1 != []:
            current.next = ListNode(l1.pop())
            current = current.next
        return value.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = int(''.join(str(x) for x in self.convertLinkedListToList(l1)))
        l2 = int(''.join(str(x) for x in self.convertLinkedListToList(l2)))
        #
        return self.convertListToLinkedList([int(x) for x in str(l1 + l2)])

        # return convertListToLinkedList(convertLinkedListToList(l1))


data1 = Solution().convertListToLinkedList([2,4,9])
data2 = Solution().convertListToLinkedList([5,6,4,9])
data = Solution().convertLinkedListToList(Solution().addTwoNumbers(data1, data2))

print(data)
