class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or s == None:
            return False
        self.s = s
        for i in range(int(len(s)/2)):
            if self._eval_(s[0:i+1]):
                return True
        return False


    def _eval_(self, s):
        if len(set(self.s.split(s))) == 1:
            return True
        else:
            return False



s = 'abcabc'
t = Solution()
ret =t.repeatedSubstringPattern(s)
print(ret)