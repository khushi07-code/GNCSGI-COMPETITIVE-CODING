
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        def traverseDFS(leftChild,rightChild,level):
            if leftChild==None or rightChild==None:
                return 
            if level%2==0:
                t=leftChild.val
                leftChild.val=rightChild.val
                rightChild.val=t
            traverseDFS(leftChild.left , rightChild.right, level+1)
            traverseDFS(leftChild.right, rightChild.left,level+1)

        traverseDFS(root.left ,root.right,0) 
        return root
