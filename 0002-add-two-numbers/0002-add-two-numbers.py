# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        ans = ListNode(0)
        curr = ans 
        carry = 0

        while l1 or l2 or carry != 0:
            num_1 = l1.val if l1 else 0
            num_2 = l2.val if l2 else 0
            add = (num_1 + num_2 + carry) % 10
            carry = (num_1 + num_2 + carry) // 10

            curr.next = ListNode(add)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        return ans.next


            
