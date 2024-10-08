# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , slow , fast = None , head , head
        if(head == None or head.next==None):
            return None
        while(fast!=None and fast.next!=None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head