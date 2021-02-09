# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root=ListNode(0)  # 建立哨兵节点
        root.next=head
        pre=root
        cur=root.next

        while cur!=None:
            if cur.val==val:
                cur=cur.next
                pre.next=cur
            else:
                pre=cur
                cur=cur.next
        return root.next