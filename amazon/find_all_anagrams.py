class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        hist = dict()
        for i in p:
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        s = list(s)
        if len(s) == 0 or len(s) < len(p):
            return ret
        p = sorted(p)
        for i in range(len(p)):
            if s[i] in hist:
                hist[s[i]] -= 1
            else:
                hist[s[i]] = -1
        if all(value == 0 for value in hist.values()):
            ret.append(0)
        for i in range(1, len(s)-len(p)+1):
            # print(i)
            head = i-1
            tail = i+len(p)-1
            if s[head] in hist:
                hist[s[head]] += 1
            else:
                hist[s[head]] = 1
            if s[tail] in hist:
                hist[s[tail]] -= 1
            else:
                hist[s[tail]] = -1
            if all(value == 0 for value in hist.values()):
                ret.append(i)
        return ret



# p = 'baa'
# s = 'aa'
# test = Solution()
# ret = test.findAnagrams(p, s)
# print(ret)