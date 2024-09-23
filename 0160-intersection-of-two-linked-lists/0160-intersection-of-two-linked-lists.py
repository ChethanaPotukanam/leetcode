# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp,temp2=headA,headB
        while(temp!=temp2):
            temp=temp.next
            temp2=temp2.next
            if(temp==None and temp2==None):
                return None
            if(temp==None):temp=headB
            if(temp2==None):temp2=headA
        return temp
        