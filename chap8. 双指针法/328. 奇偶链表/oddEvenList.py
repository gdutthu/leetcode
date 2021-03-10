# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head

        # 初始化奇数节点的链表、头结点
        odd_root=head
        odd_node=odd_root

        # 初始化偶数数节点的链表、头结点
        even_root=head.next
        even_node=even_root

        head=head.next.next

        index=3
        while head!=None:
            if index %2==0:
                even_node.next=head
                even_node=even_node.next
            else:
                odd_node.next=head
                odd_node=odd_node.next
            index +=1
            head=head.next
        odd_node.next=even_root
        even_node.next=None
        return odd_root