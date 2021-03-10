# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head
        # step1:按照要求收集节点
        less = []
        others = []
        while head != None:
            if head.val < x:
                less.append(head)
            else:
                others.append(head)
            head = head.next

        # step2：重新连接节点
        arr = []
        for index in range(len(less)):
            arr.append(less[index])
        for index in range(len(others)):
            arr.append(others[index])
        for index in range(len(arr) - 1):
            arr[index].next = arr[index + 1]
        arr[-1].next = None
        return arr[0]