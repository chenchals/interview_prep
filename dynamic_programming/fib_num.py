class Solution(object):
    def __init__(self):
        self.lookup = {}

    def fib(self, n):
        if n <= 1:
            return n
        else:
            if n in self.lookup:
                return self.lookup[n]
            else:
                ret = self.fib(n-1)+self.fib(n-2)
                self.lookup[n] = ret
                return ret


t = Solution()
ret = t.fib(6)
print(ret)