# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_r = 0
        def maxDepth(node):
            if not node:
                return 0
            l = maxDepth(node.left)
            r = maxDepth(node.right)
            if self.max_r < (l+r):
               self.max_r =  l+r
            return 1+max(l,r)
        maxDepth(root)
        return self.max_r
        



        