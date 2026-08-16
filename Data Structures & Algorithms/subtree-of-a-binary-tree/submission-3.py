# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if (not p and not q) :
            return True
        if p.val != q.val:
            return False
        if self.isSameTree(p.left,q.left) == False:
            return False

        if self.isSameTree(p.right,q.right) == False:
            return False
        return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not subRoot:
            return True
        if root.val == subRoot.val:
            if self.isSameTree(root,subRoot)==True:
                return True

        if self.isSubtree(root.left,subRoot)==True:
            return True
        if self.isSubtree(root.right,subRoot)==True:
            return True
        return False

        
        