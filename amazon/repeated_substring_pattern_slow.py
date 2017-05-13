import sys
sys.setrecursionlimit = 1000*1000*1000
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.look_up = dict()
        self.s = s
        start = None
        cur = 0
        return self._impl_(start,cur)

    def _impl_(self, start, cur, ):
        if cur >= len(self.s):
            return False
        if start is not None:
            # end here
            s = self.s[start:cur]
            if s in self.look_up:
                left = self.look_up[s]
            else:
                left = self._eval_(s)
            # continue
            right = self._impl_(start, cur+1)
            return left or right
        else:
            # skip
            left = self._impl_(None, cur+1)
            # choose this to start
            right = self._impl_(cur, cur+1)
            return left or right

    def _eval_(self, s):
        if len(set(self.s.split(s))) == 1:
            self.look_up[s] = True
            return True
        else:
            self.look_up[s] = False
            return False



s = 'abcabc'
t = Solution()
ret =t.repeatedSubstringPattern(s)
print(ret)