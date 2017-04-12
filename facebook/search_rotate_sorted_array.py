class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        m = (l+r)/2
        if nums[m] == target:
            return m
        elif nums[l] < nums[m]:
            if nums[m] > target > nums[l]:
                pass
            elif target:
                pass
        else:
            pass