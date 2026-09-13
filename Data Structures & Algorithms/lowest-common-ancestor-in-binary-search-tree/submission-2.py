# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        if (p.val>=root.val and q.val<=root.val)or(p.val<=root.val and q.val>=root.val):
            return root

        l = self.lowestCommonAncestor(root.left,p,q)
        if l:
            return l
        r = self.lowestCommonAncestor(root.right,p,q)
        return r






        # if (root.val==p.val and(( root.left and root.left.val == q.val) or ( root.right and root.right.val == q.val))):
        #     print('bbbbbb')
        #     return root
        # if (root.val==q.val and(( root.left and root.left.val == p.val) or ( root.right and root.right.val == p.val))):
        #     print('aaaaaaaa')
        #     return root
        # if ( root.left and  root.right) and( (root.left.val == p.val and root.right.val == q.val) or (root.left.val == q.val and root.right.val == p.val)):
           
        #     return root
        # l = self.lowestCommonAncestor(root.left,p,q)
        # if l:
        #     return l
        # r = self.lowestCommonAncestor(root.right,p,q)
        # return r
