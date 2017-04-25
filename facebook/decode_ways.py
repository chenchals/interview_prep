class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1 # use this as a buffer to add the extra solution for each current i
        dp[1] = dp[0] if s[0] != '0' else 0
        for i in range(2, len(dp)):
            first = int(s[i-1])
            second = int(''.join(s[i-2:i]))
            if first != 0:
                dp[i] += dp[i-1]
            if 10 <= second <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]

test = Solution()

test.numDecodings('012')