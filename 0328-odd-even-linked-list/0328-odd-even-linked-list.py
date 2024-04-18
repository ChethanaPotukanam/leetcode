# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None or head.next.next==None):
            return head
        head2=head.next
        temp,temp2=head,head2
        while temp2 and temp2.next:
            temp.next,temp2.next=temp.next.next,temp2.next.next
            temp,temp2=temp.next,temp2.next
        temp.next=head2
        return head
        ##Method##
        # length=0
        # n=head
        
        # while n is not None:
        #     length+=1
        #     n=n.next
        # if(head==None or length==1):
        #     return head
        # n=head
        # oddval=[]
        # evenval=[]
        # i=0
        # while n is not None:
        #     i+=1
        #     if(i%2==0):
        #         evenval.append(n.val)
        #     else:
        #         oddval.append(n.val)
        #     n=n.next
        # values=oddval+evenval
        # n=head
        # i=0
        # while n is not None:
        #     n.val=values[i]
        #     i+=1
        #     n=n.next
        # return head