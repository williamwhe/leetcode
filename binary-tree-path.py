class Solution(object):
    def dfs(self, root, cur, retval):
        if root is None:
            return
        if root.left is None and root.right is None:
            cur.append(root.val)
            retval.append("->".join(map(str,cur)))
            return
        if root.left is not None:
            self.dfs(root.left, cur+[root.val], retval)
        if root.right is not None:
            self.dfs(root.right, cur+[root.val], retval)
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        cur=[]
        retval=[]
        self.dfs(root, cur, retval)
        return retval
        
s=Solution()
print s.binaryTreePaths(root)