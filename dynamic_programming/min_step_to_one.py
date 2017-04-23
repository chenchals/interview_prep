import sys
class MinStepsToOne(object):
    def __init__(self):
        self.mem = {1:1}

    def recursion(self, n):
        if n in self.mem:
            return self.mem[n]
        ret = 1+self.recursion(n - 1)
        if n % 2 == 0:
            ret = min(ret, 1+self.recursion(int(n/2)))
        if n % 3 == 0:
            ret = min(ret, 1+self.recursion(int(n/3)))
        self.mem[n] = ret
        return self.mem[n]

    def dp(self, n):
        for i in range(2, n+1):
            if i-1 in self.mem:
                step = self.mem[i-1] + 1
            if i%2:
                if int(i/2) in self.mem:
                    step = min(step, self.mem[int(i/2)]+1)
            if i%3:
                if int(i/3) in self.mem:
                    step = min(step, self.mem[int(i/3)]+1)
            self.mem[i] = step
        return self.mem[n]

t = MinStepsToOne()
# print(t.recursion(999))
print(t.dp(110999))