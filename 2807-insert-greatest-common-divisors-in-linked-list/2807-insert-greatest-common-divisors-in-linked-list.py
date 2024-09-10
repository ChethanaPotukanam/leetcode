# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y):
            while(y):
                x,y = y,x%y
            return x
        if not head.next :
            return head
        prev , cur = head , head.next
        while(cur!=None):
            gcd_val = gcd(prev.val , cur.val)
            node = ListNode(gcd_val , cur)
            prev.next = node
            prev = cur
            cur = cur.next
        return head 
        