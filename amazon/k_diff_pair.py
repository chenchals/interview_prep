# https://leetcode.com/problems/k-diff-pairs-in-an-array/#/description

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k < 0:
            return 0
        count = 0
        look_up = dict()
        for i in nums:
            if i in look_up:
                look_up[i] += 1
            else:
                look_up[i] = 1
        if k != 0:
            for x in nums:
                if (x+k in look_up):
                    count += 1
        if k == 0:
            count = sum([1 for v in look_up if look_up[v] > 1])
        return count


test = Solution()
ret = test.findPairs([3,1,1,3,4], 0)
print(ret)