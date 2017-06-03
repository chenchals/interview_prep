class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.root = root
        self.ret = []
        self.ret.append(root.val)
        self.dfs_left_boundary(root.left)
        self.dfs_leaves(root)
        self.dfs_right_boundary(root.right)
        return self.ret

    def dfs_left_boundary(self, node):
        if node is None or (node.left is None and node.right is None):
            return
        self.ret.append(node.val)
        if node.left:
            self.dfs_left_boundary(node.left)
        else:
            self.dfs_right_boundary(node.right)


    def dfs_right_boundary(self, node):
        if node is None or (node.left is None and node.right is None):
            return
        self.ret.append(node.val)
        if node.right:
            self.dfs_right_boundary(node.right)
        else:
            self.dfs_right_boundary(node.left)

    def dfs_leaves(self, node):
        if not node:
            return
        # all the way down to leaf nodes
        if node != self.root and node.left is None and node.right is None:
            self.ret.append(node.val)
        self.dfs_leaves(node.left)
        self.dfs_leaves(node.right)