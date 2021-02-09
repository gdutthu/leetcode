# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            node1 = lists.pop(0)
            node2 = lists.pop(0)
            newNode = self.mergeTwoLists(node1, node2)
            lists.append(newNode)
        return lists[0]

    # 函数功能：合并两个升序链表
    def mergeTwoLists(self, node1, node2):
        root = ListNode(0)
        cur = root

        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                cur.next = node1
                node1 = node1.next
                cur = cur.next
            else:
                cur.next = node2
                node2 = node2.next
                cur = cur.next

        if node1 != None:
            while node1 != None:
                cur.next = node1
                node1 = node1.next
                cur = cur.next
        else:
            while node2 != None:
                cur.next = node2
                node2 = node2.next
                cur = cur.next
        return root.next