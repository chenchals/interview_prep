class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        self.dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            self.dp[i][i] = 1
        return self.lps(s, 0, len(s)-1)

    def lps(self, s, i, j):
        if self.dp[i][j] is not None:
            return self.dp[i][j]
        if i > j:
            return 0
        if j==i+1 and s[j]==s[i]:
            ret = 2
        elif s[i] == s[j]:
            ret = self.lps(s, i+1, j-1) + 2
        else:
            ret = max(self.lps(s,i+1, j), self.lps(s,i, j-1))
        self.dp[i][j] = ret
        return self.dp[i][j]



a = 'abbaaaa'
t = Solution()
ret = t.longestPalindromeSubseq(a)
print(ret)