# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        node={}  # 记录已出现的节点数值
        arr=[]
        # step1：储存位重复出现的节点
        while head !=None:
            if head.val not in node:
                node[head.val]=1
                arr.append(head)
            elif head.val in node:
                while len(arr)>0 and arr[-1].val ==head.val:
                    arr.pop()
            head=head.next
        # step2:将所得新节点重新连接
        length=len(arr)
        if length>=1:
            for index in range(length-1):
                arr[index].next=arr[index+1]
            arr[-1].next=None
            return arr[0]
        else:
            return None