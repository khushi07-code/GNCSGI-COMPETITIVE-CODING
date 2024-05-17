# delete only leaf odes that is equal to terget value

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if(root==None):
            return
        root.left=self.removeLeafNodes(root.left,target)
        root.right=self.removeLeafNodes(root.right,target)
        if(root.val==target and root.left==None and root.right==None):
            return None
        return root
