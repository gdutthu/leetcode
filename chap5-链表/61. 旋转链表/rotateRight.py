# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head
        # step1:存储列表元素
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        length = len(array)

        # step2：列表数组进行右旋转
        newArr = [0] * length
        for index in range(length):
            newIndex = (index + k) % length
            newArr[newIndex] = ListNode(array[index])

        # step3：连接新数组
        for index in range(length - 1):
            newArr[index].next = newArr[index + 1]
        return newArr[0]