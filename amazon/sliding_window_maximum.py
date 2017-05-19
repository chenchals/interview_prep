from collections import deque

def h(seq):
    #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    #by unutbu
    return sorted(range(len(seq)), key=seq.__getitem__)

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        # window_buf = nums[:k]
        # dq = deque(h(window_buf))
        # print('=',dq)
        # ret = [nums[dq[-1]]]
        dq = deque()
        ret = []
        i = 0
        while i < len(nums):
            # print(i, k, nums, dq, dq[0], end=' -- ')
            if len(dq) > 0 and dq[-1] <= i-k:
                dq.pop()
            while len(dq) > 0 and (nums[i] > nums[dq[0]]):
                # print(dq)
                dq.popleft()
            # print(i, k, nums, dq,)
            dq.appendleft(i)
            # print(dq, nums[dq[0]])
            if i >= k-1:
                ret.append(nums[dq[-1]])
            i += 1
        return ret


t = Solution()
# ret = t.maxSlidingWindow([1,3,1,2,0,5], 3)
ret = t.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(ret)