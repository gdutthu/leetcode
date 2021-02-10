# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        root = ListNode(0)
        cur = root
        res = 0

        while l1 != None and l2 != None:
            item = l1.val + l2.val + res
            cur.next = ListNode(item % 10)
            res = item // 10

            # 节点移动
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        # 此时至少有一个链表遍历结束
        if l1 != None:
            while l1 != None:
                item = l1.val + res
                cur.next = ListNode(item % 10)
                res = item // 10

                # 节点移动
                cur = cur.next
                l1 = l1.next
        else:
            while l2 != None:
                item = l2.val + res
                cur.next = ListNode(item % 10)
                res = item // 10

                # 节点移动
                cur = cur.next
                l2 = l2.next

        if res != 0:
            cur.next = ListNode(res)

        return root.next