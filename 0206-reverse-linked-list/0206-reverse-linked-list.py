# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        if(head):temp2 = head.next
        while(temp):
            temp.next=prev
            prev=temp
            temp=temp2
            if(temp):temp2=temp.next
        head=prev
        return head