class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        # reverse this string first
        s = ''.join(s[::-1])
        ret = []
        for each in s.split(' '):
            ret.append(each[::-1])

        return ' '.join(ret)


