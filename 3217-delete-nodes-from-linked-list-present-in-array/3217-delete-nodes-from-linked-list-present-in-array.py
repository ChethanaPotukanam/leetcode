# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return head
        nums_set = set(nums)
        dummyNode = ListNode(0)
        dummyNode.next = head
        prev , temp = dummyNode , head
        while(temp!=None):
            if(temp.val in nums_set):
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return dummyNode.next