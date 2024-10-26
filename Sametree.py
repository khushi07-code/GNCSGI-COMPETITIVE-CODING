# Given the roots of two binary trees p and q, write a function to check if they are the same or not.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(r1,r2):
            if r1==None and r2==None:
                return True
            if r1==None and r2 or r2==None and r1:
                return False
            if r1.val!=r2.val:
                return False       
            f1=dfs(r1.left,r2.left)
            f2=dfs(r1.right,r2.right)
            return f1 and f2
                
        flag=dfs(p,q)
        return flag
        
