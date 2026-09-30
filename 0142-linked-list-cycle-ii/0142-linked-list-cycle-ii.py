# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        seen = set()
        
        node = head
        while node:
            if not node in seen:
                seen.add(node)
            else:
                return node
            node = node.next
 
        return None 

        


        '''
        if not head or not head.next:
            return None
        
        slow, fast = head, head

        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break 
            if not fast:
                break
        
        if slow != fast:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow 
        '''