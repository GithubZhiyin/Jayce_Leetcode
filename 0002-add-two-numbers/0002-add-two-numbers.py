# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        ans = ListNode(0)
        curr = ans 
        add_ = 0 
        while l1 and l2:
            sum_ = (l1.val + l2.val + add_) % 10
            add_ = (l1.val + l2.val + add_) // 10
            curr.next = ListNode(sum_)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            sum_ = (l1.val + add_) % 10
            add_ = (l1.val + add_) // 10
            curr.next = ListNode(sum_)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            sum_ = (l2.val + add_) % 10
            add_ = (l2.val + add_) // 10
            curr.next = ListNode(sum_)   
            curr = curr.next
            l2 = l2.next
        
        if add_ > 0:
            curr.next = ListNode(add_)

        return ans.next
