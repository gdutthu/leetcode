# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node={}
        while head!=None:
            if head not in node:
                node[head]=1
            else:
                return True
            head=head.next
        return False