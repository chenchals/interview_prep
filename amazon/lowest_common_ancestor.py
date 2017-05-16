# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # this line make sure that p and q in the same side of root (same child tree)
        while (root.val - p.val) * (root.val - q.val) > 0:
            # if on the left side (root is bigger than whatever one of them)
            if root.val > p.val:
                root = root.left
            else: # else on the right side
                root = root.right
        # if the root is in between of one of the p and q, return the root
        return root