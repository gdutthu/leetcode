# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_arr, l2_arr = [], []
        while l1 != None:
            l1_arr.append(l1.val)
            l1 = l1.next

        while l2 != None:
            l2_arr.append(l2.val)
            l2 = l2.next

        res = 0
        reult = []
        while len(l1_arr) > 0 or len(l2_arr) > 0:
            item = res
            if len(l1_arr) > 0:
                item += l1_arr.pop()
            if len(l2_arr) > 0:
                item += l2_arr.pop()
            reult.append(ListNode(item % 10))
            res = item // 10
        if res != 0:
            reult.append(ListNode(res))

        # 翻转列表
        length = len(reult)
        for index in range(length // 2):
            reult[index], reult[length - 1 - index] = reult[length - 1 - index], reult[index]

        # 连接链表
        for index in range(length - 1):
            reult[index].next = reult[index + 1]

        return reult[0]