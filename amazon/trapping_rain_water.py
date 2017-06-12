class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        This is the idea, calculate the amount of water trapped in current index, and sum them all together.
        To calculate the amount of water trapped in current index is to use min(highest_left, highest_right) minus the value in current index.
        '''
        if len(height) <= 2:
            return 0
        left_h = height[:]
        right_h = height[:]
        # build left
        for i in range(1, len(height)):
            if left_h[i] > left_h[i - 1]:
                continue
            else:
                left_h[i] = left_h[i - 1]

        # build right
        for i in reversed(range(0, len(height) - 1)):
            if right_h[i] < right_h[i + 1]:
                right_h[i] = right_h[i + 1]
            else:
                continue
        ret = 0
        # sum over all value
        for i in range(1, len(height) - 1):
            bar = min(left_h[i], right_h[i])
            cur = max(0, bar - height[i])
            ret += cur
        return ret




s = Solution()
inputs = [2,0,2]
ret = s.trap(inputs)
print(ret)