import pdb

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif sum == root.val and root.left is None and root.right is None:
            return True
        elif root.left is None and root.right is None:
            return False
        elif root.right is None:
            return self.hasPathSum(root.left, sum-root.val)
        elif root.left is None:
            return self.hasPathSum(root.right, sum-root.val)
        else:
            #pdb.set_trace()
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

s = Solution()
root = TreeNode(1)
left = TreeNode(-2)
right = TreeNode(3)
root.left = left
root.right = right
print s.hasPathSum(root, -1)
