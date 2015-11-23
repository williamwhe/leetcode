import copy, pdb

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        top2bottom = []
        prev = [root]
        while len(prev) > 0:
            top2bottom.append(prev)
            curr = []
            for node in prev:
                if node.left is not None:
                    curr.append(node.left)
                if node.right is not None:
                    curr.append(node.right)
            prev = copy.copy(curr)
        #pdb.set_trace()
        bottom2top = []
        for nodes in reversed(top2bottom):
            curr = []
            for node in nodes:
                curr.append(node.val)
            bottom2top.append(curr)
        return bottom2top

s = Solution()
print s.levelOrderBottom(None)
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
print s.levelOrderBottom(root)