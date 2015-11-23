import math

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
    		return 1
    	elif root.left is None:
    	    return 1+self.minDepth(root.right)
    	elif root.right is None:
    	    return 1+self.minDepth(root.left)
    	else:
    	    return min(1+self.minDepth(root.left), 1+self.minDepth(root.right))

s = Solution()
root = None
print s.minDepth(root)