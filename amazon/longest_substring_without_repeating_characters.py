class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hist = set()
        best = 0
        head, tail = 0, 0
        while tail < len(s):
            if s[tail] in hist:
                # found duplicate, set head to tail
                best = max(best, tail-head)
                # move head
                while s[head] != s[tail]:
                    hist.remove(s[head])
                    head += 1
                # do not need to remove the current char, because it's the repeated one, remove one and add one is do nothing
                head += 1
            else:
                hist.add(s[tail])
            tail += 1
        if tail == len(s):
            return max(best, tail-head)
        return best


t = Solution()
input = ''
ret = t.lengthOfLongestSubstring(input)
print(ret)