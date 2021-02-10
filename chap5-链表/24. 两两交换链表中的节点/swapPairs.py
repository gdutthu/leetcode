# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        index=0
        arr=[]
        while head!=None:
            arr.append(head)
            head=head.next
        length=len(arr)

        index=0
        while index+1<length:
            arr[index],arr[index+1]=arr[index+1],arr[index]
            index +=2
        for index in range(length-1):
            arr[index].next=arr[index+1]
        arr[-1].next=None
        return arr[0]