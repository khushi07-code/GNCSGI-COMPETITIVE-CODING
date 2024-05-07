# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(r):
            prev = None
            current = r
            while current:
                 temp = current.next
                 current.next = prev
                 prev = current
                 current = temp
            return prev


        answer=ListNode()
        temp2=answer
        temp=reverse(head)
        r=0
        while temp:
            temp2.next=ListNode((((temp.val)*2)%10)+r)
            temp2=temp2.next
            r=(temp.val*2)//10
            temp=temp.next
        if(r!=0):
            temp2.next=ListNode(r)
        answer=answer.next
        answer=reverse(answer)
        return answer
# input 198
# output 378 
