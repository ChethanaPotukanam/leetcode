# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow,fast = dummy,head
        for i in range(0,n,1):
            fast = fast.next
        if(fast == None):
            return head.next
        while(fast!=None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head