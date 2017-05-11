class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1, c2, c3 = 0,0,0
        stack = list()
        pre = None
        for i in s:
            if i == '(':
                c1 += 1
                pre = i
                # stack.append(i)
            elif i == ')' and c1 == 0 and pre != '(':
                return False
            elif i == ')' and c1 > 0 and pre == '(':
                c1 -= 1
            if i == '{':
                c2 += 1
                pre = i
            elif i == '}' and c2 == 0 and pre != '{':
                return False
            elif i == '}' and c2 > 0 and pre == '{':
                c2 -= 1
            if i == '[':
                c3 += 1
                pre = i
            elif i == ']' and c3 == 0 and pre != '[':
                return False
            elif i == ']' and c3 > 0 and pre == '[':
                c3 -= 1
            # print(c1, c2, c3)
        return (not c1) and (not c2) and (not c3)



t = Solution()
print(t.isValid('()'))