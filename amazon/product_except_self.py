class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = list()
        p = 1
        for i in range(len(nums)):
            ret.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= p
            p *= nums[i]
        return ret

t = Solution()
i = [1,2,3]
ret = t.productExceptSelf(i)
print(ret)