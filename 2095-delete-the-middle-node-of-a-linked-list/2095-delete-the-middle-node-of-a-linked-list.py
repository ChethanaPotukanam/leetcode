# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return head
        else:
            length=0
            n=head
            while n is not None:
                n=n.next
                length+=1
            if length==1:
                return None
            m=length//2
            h=head
            for i in range(m-1):
                h=h.next
            h.next=h.next.next
            return head