# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r=merge=ListNode()
        p=list1
        q=list2
        while p!=None and q!=None:
            if p.val<=q.val:
                r.next=ListNode(p.val)
                p=p.next
                r=r.next
            else:
                r.next=ListNode(q.val)
                q=q.next
                r=r.next
        while p!=None:
            r.next=ListNode(p.val)
            r=r.next
            p=p.next
        while q!=None:
            r.next=ListNode(q.val)
            r=r.next
            q=q.next
        merge=merge.next
        return merge

