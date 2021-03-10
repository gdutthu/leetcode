# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        pre=head
        root=head.next
        while root !=None:
            if pre.val !=root.val:
                pre=root
                root=root.next
            elif pre.val==root.val:
                root=root.next
                pre.next=root
        return head