# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        cur = root

        # 采用外排法合并链表
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        # 此时至少有一个链表已经遍历结束
        if l1 != None:
            while l1 != None:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
        else:
            while l2 != None:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        return root.next