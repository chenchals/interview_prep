class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        s = list(s)
        p = sorted(p)
        for i in range(len(s)):
            window = sorted(s[i:i+len(p)])
            # print(window, p)
            if window == p:
               ret.append(i)
        return ret



p = 'abab'
s = 'ab'
test = Solution()
ret = test.findAnagrams(p, s)
print(ret)