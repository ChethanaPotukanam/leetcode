# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        temp2 = l2
        dummy = ListNode() 
        cur = dummy
        carry = 0
        while(temp or temp2):
            s=carry
            if(temp): 
                s+=temp.val
                temp = temp.next
            if(temp2): 
                s+=temp2.val
                temp2 = temp2.next
            data = s%10
            n = ListNode(data)
            carry = s//10
            cur.next = n
            cur = n
        if(carry): 
            n=ListNode(carry)
            cur.next=n
        return dummy.next
