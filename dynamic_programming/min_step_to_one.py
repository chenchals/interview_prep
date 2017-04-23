class MinStepsToOne(object):
    def __init__(self):
        self.mem = {}
    def recursion(self, n, step):
        if n == 1:
            return self.mem[n]

    def dp(self, n):
        pass


t = MinStepsToOne()
print(t.recursion(1, 0))