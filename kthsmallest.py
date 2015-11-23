# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodes = self.toList(root)
        return nodes[k]
    
    def toList(self, root):
        if root is None:
            return []
        leftlist = self.toList(root.left)
        rightlist = self.toList(root.right)
        return leftlist.extend([root.val]).extend(rightlist)