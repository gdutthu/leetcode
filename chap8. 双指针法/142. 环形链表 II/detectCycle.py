# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node={}
        while head!=None:
            if head not in node:
                node[head]=1
            else:
                return head
            head =head.next
        return None