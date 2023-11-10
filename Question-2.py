# Question 2
# Maximum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between
# the values of any two different nodes in the tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def minDiffInBST(root):
        prev, res = None, float('inf')
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return res
if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print(TreeNode.minDiffInBST(root))