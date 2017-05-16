class Solution(object):
    def longestPalindrome(self, s):
        if s == '':
            return ''
        lookup = [[False for _ in range(len(s))] for _ in range(len(s))]
        best = ''
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i < 3:
                        lookup[i][j] = True
                    elif lookup[i+1][j-1]:
                        lookup[i][j] = True
                if j-i > len(best)-1 and lookup[i][j]:
                    best = s[i:j+1]
        # for v in lookup:
        #     print(v)
        return best


t = Solution()
ret = t.longestPalindrome('leetcoeeeaocte')
print(ret)
# for v in ret:
#     print(v)

