# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def dfs(root):
    if root is None:
        return True, None, None


    if root.left is not None:
        l_ret, l_left, l_right = dfs(root.left)
    else:
        l_ret, l_left, l_right = True, root.val, root.val

    if root.right is not None:
        r_ret, r_left, r_right = dfs(root.right)
    else:
        r_ret, r_left, r_right = True, root.val, root.val

    if not l_ret and not r_ret:
        return False, root.val, root.val

    return (l_left < root.val < r_right), max(l_left, root.val), min(r_right, root.val)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        ret = dfs(root)
        return ret[0]