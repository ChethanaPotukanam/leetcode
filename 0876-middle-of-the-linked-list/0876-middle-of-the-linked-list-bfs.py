# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,n=head,0
        while(temp != None):
            temp = temp.next
            n+=1
        mid=(n//2)+1-1
        temp = head
        for i in range(mid):
            temp = temp.next
        return temp
