# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # solution_1: Using set to collect the visted nodes
        seen = set()
        curr = head
        while curr:
            seen.add(curr)
            curr = curr.next
            if curr in seen:
                return True
        return False


        

        