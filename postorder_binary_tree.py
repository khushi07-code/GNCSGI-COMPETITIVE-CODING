# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]
        def post(p,a):
            if p==None:
                return a
            a=post(p.left,a)
            a=post(p.right,a)
            a.append(p.val)
            return a
        return post(root,answer)
