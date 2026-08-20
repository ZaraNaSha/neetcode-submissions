# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(t,left,right):
            if not t:
                return True
            
            if not(left < t.val < right):
                return False
            
            return valid(t.left,left,t.val) and  valid(t.right,t.val,right)

        return valid(root,float("-inf"), float("inf"))