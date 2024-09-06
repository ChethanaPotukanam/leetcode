# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev , cur = None , head
            while(cur!=None):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        slow , fast = head , head
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        first = head
        second = reverse(slow.next)
        while(second != None):
            if(first.val != second.val):
                return False
            first=first.next
            second=second.next
        return True