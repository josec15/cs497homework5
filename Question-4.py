# Question 4
# Binary Tree Maximum Path Sum

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
# has an edge connecting them. A node can only appear in the sequence at most once. Note that
# the path does not need to pass through the root. The path sum of a path is the sum of the 
# node's values in the path. Given the root of a binary tree, return the maximum path sum
# of any non-empty path.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def maxPathSum(root):
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(TreeNode.maxPathSum(root))