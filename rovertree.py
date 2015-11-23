import pdb,operator,copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if root is None:
            return None
        nodes=[]
        st=[]
        self.dfs(root, nodes)
        snodes=[]
        for n in nodes:
            snodes.append(copy.deepcopy(n))
        snodes.sort(key=operator.attrgetter('val'))
        for i in range(len(nodes)):
            nodes[i].val=snodes[i].val
        return root
        
    def dfs(self, root, nodes):
        if root is None:
            return
        self.dfs(root.left, nodes)
        nodes.append(root)
        self.dfs(root.right, nodes)

s=Solution()
root=TreeNode(0)
leftleaf=TreeNode(1)
root.left=leftleaf
s.recoverTree(root)