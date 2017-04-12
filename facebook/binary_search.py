class BinarySearch(object):


    def recursive(self, li, target, l, r):
        m = int((l+r)/2)
        # print(m)
        if target == li[m]:
            return m
        elif li[m] > target >= li[l]:
            return self.recursive(li, target, l, m-1)
        elif li[r] >= target > li[m]:
            return self.recursive(li, target, m+1, r)

    def loop(self, li, target):
        l = 0
        r = len(li) - 1
        while l <= r:
            m = int((l+r)/2)
            if target == li[m]:
                return m
            elif li[l] <= target < li[m]:
                r = m-1
            elif li[m] < target <= li[r]:
                l = m+1
            else:
                return None

    # todo @charles, implement these 3 methods
    def thirdMethod(self):
        pass

    def fourthMethod(self):
        pass

    def fifthMethod(self):
        pass

test = BinarySearch()
dat = [1,3,5,12]
dat = [1,2,12,13,111]
target = 111
ret = test.recursive(dat, target, 0, len(dat)-1)
print(ret)
ret = test.loop(dat, target)
print(ret)