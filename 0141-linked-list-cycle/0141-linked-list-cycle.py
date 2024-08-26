# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        l=[]
        while(temp.next not in l):
            if(temp.next is None):
                return False
            l.append(temp.next)
            temp=temp.next
        return True