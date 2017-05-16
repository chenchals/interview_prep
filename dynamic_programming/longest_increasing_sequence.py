class Solution(object):
    def __init__(self):
        self.lookup = []
        self.dp = {0:1}

    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return len(nums)
        # self.lookup = [1 for _ in nums]
        # self.lookup[0] = 0
        # self.lookup[1] = 1
        # return self._impl_(nums)
        return self._impl_recursive_(nums, len(nums)-1)

    def debug(self, nums):
        self.lookup = [1 for _ in nums]
        return self._impl_(nums)

    def _impl_recursive_(self, nums, n):
        '''
        :param nums: list of nums
        :param n: ending index
        :return: LIS
        '''
        # if n < 2:
        #     return n
        cur = n
        best = 1
        for i in range(cur): # not need n-1, because exclusive
            if i in self.dp:
                sub_answer = self.dp[i]
            else:
                sub_answer = self._impl_recursive_(nums, i) # right side is exclusive, implies i-1
                self.dp[i] = sub_answer
            print('>>>>',(i, cur), (nums[i], nums[cur]), best, sub_answer, self.dp)
            if sub_answer + 1 > best and nums[cur] > nums[i]:
                best = sub_answer + 1
        self.dp[cur] = best
            # print('<<<<',(i, n-1), (nums[i], nums[n - 1]), best, sub_answer + 1, self.dp)
        return best


    def _impl_(self,nums):
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and self.lookup[j]+1 > self.lookup[i]:
                    # print(self.lookup,nums[i],nums[j], (i, j))
                    self.lookup[i] = self.lookup[j]+1
                    # print('=',self.lookup,nums[i],nums[j], (i, j))

        return max(self.lookup)





t = Solution()
inputs = [1,2,3,4,5,6,7,8,9,10,11,16,15,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
inputs = [1,3,6,7,9,4,10,5,6]
# inputs = [1,3,6]
# inputs = [1,3,6,7,8,9]
# inputs = [10,9,2,5,3,7,101,18]
# inputs = [2,2]
# inputs = [1,3,4,2]
# inputs = [4,10,4,3,8,9]
ret = t.lengthOfLIS(inputs)
# for each in t.lookup:
#     print(each, t.lookup[each])
print(ret, t.debug(inputs))