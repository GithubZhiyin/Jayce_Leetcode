# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head

        node1, node2 = dummy, head
        while node2 and node2.next:
            node1.next = node2.next
            curr = node2.next.next
            node2.next.next = node2
            node2.next = curr
            node1, node2 = node2, node2.next
        
        return dummy.next 

            
            
