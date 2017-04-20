def i_to_s(n):
    next = n
    output = []
    while next > 0:
        # convert 1-26 to 0-25
        cur = (next-1)%26
        print(next, cur)
        output.append(chr(cur+97))
        next = int(round((next-cur)/26))
    # print(''.join(reversed(output)))

    return ''.join(reversed(output)).upper()

# ret = i_to_s(111)
# print(ret)
# exit()

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return i_to_s(n)