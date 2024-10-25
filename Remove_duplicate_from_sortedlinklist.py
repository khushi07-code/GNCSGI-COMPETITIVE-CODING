# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        r=head.next
        p=result=ListNode(head.val)
        while r!=None:
            if  r.val!=p.val:
                p.next=ListNode(r.val)
                p=p.next
            r=r.next
        return result
        

