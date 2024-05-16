class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def stackimpl(tree):
           if(tree==None):
                return 
           stack.append(tree.val)
           stackimpl(tree.left)
           stackimpl(tree.right)
           

        stack=[]
        value=[]
        stackimpl(root)
        while stack:
            val=stack.pop()
            if(val==2):
                v1=value.pop()
                v2=value.pop()
                value.append(v1 or v2)
            elif(val==3):
                v1=value.pop()
                v2=value.pop()
                value.append(v1 and v2)
            else:
                value.append(val)
        return value.pop()
