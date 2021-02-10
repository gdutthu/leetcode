# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        arr = []
        while head != None:
            arr.append(head)
            head = head.next
        length = len(arr)

        for index in range(length // 2):
            arr[index], arr[length - index - 1] = arr[length - index - 1], arr[index]

        for index in range(length - 1):
            arr[index].next = arr[index + 1]
        arr[-1].next = None
        return arr[0]