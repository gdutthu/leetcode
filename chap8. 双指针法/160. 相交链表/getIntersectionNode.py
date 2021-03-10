# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # step1:分别计算两个链表的长度
        node1, node2 = headA, headB
        length1, length2 = 0, 0
        while node1 != None:
            length1 += 1
            node1 = node1.next
        while node2 != None:
            length2 += 1
            node2 = node2.next

        # step2：让长链表先走
        gap = length1 - length2
        if gap > 0:
            for i in range(gap):
                headA = headA.next
        elif gap < 0:
            for i in range(abs(gap)):
                headB = headB.next

        # step3:寻找链表交点
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None