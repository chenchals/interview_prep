class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(x) for x in a.split()]
        b = [int(x) for x in b.split()]
        buf = 0
        ret = a if len(a) > len(b) else b
        a_ind = len(a)-1
        b_ind = len(b)-1
        while a_ind >= 0 and b_ind >= 0:
            sum = a[a_ind] + b[b_ind]
            sum += buf
            rem = sum % 2
            buf = sum / 2
            ret[a_ind if a_ind > b_ind else b_ind] = rem
            # if sum == 2:
            #     ret.insert(buf,0)
            #     buf = 1
            # else:
            #     ret.insert(sum, 0)
            a_ind -= 1
            b_ind -= 1
        return ''.join([str(x) for x in ret])

test = Solution()
ret = test.addBinary('11', '1')
print(ret)