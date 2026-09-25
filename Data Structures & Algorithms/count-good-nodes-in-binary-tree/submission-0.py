# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #maxv = 0
        self.res = 0
        def dfs(node,maxv):
            if not node:
                return
            if node.val >= maxv:
                print(node.val)
                self.res += 1
            maxv = max(maxv,node.val) 
            dfs(node.left,maxv)
            #self.res.pop()
            dfs(node.right,maxv)
        dfs(root,root.val)
        return self.res

        