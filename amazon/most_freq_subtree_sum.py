# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.freq_lookup = {
        }
        self.sub_tree_sum(root)
        most_freq = max(self.freq_lookup.values())
        # print(self.freq_lookup)
        ret = []
        for key, value in self.freq_lookup.items():
            if value == most_freq:
                ret.append(key)
        return ret

    def sub_tree_sum(self, root):
        if root is None:
            return 0
        tree_sum = self.sub_tree_sum(root.left) +  self.sub_tree_sum(root.right) + root.val
        if tree_sum in self.freq_lookup:
            self.freq_lookup[tree_sum] += 1
        else:
            self.freq_lookup[tree_sum] = 1
        return tree_sum