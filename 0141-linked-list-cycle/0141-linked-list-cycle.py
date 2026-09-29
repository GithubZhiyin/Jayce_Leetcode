# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # solution.2 Using Floyd's circle

        if not head or not head.next:
            return False
        
        fast = head.next
        slow = head

        while fast != slow and fast.next:
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
            slow = slow.next 
        return fast == slow
            



        

        