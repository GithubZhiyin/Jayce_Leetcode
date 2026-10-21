# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        ans = ListNode(0)
        curr = ans

        p = [list_ for list_ in lists] 

        while True:
            min_i = -1
            for i, node in enumerate(p):
                if not node:
                    continue
                if min_i == -1 or node.val < p[min_i].val:
                        min_i = i 
            if min_i == -1:
                break
  
            curr.next = p[min_i]
            curr = curr.next
            p[min_i] = p[min_i].next
        
        return ans.next
                

                