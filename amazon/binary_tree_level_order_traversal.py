# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        # this stack keep tracks nodes in current level
        parent_stack = []
        # this stack tracks nodes in child level
        child_stack = []
        parent_stack.append(root)
        while len(parent_stack) != 0:
            cur_level = []
            for each in parent_stack:
                cur_level.append(each.val)
                if each.left:
                    child_stack.append(each.left)
                if each.right:
                    child_stack.append(each.right)
            # for each level, replace parent level stack with child level stack
            parent_stack = child_stack
            # and clean child level stack
            child_stack = list()
            ret.append(cur_level)
        return ret
