def max_sum_table(li, k):
    # sum the first row
    result = 0
    # init
    for j in range(0, len(li)):
        sum = 0
        # upper diagonal
        for i in range(j, len(li)):
            sum += li[i]
            if sum == k:
                result = max(result, i-j+1)
    return result

def max_sum_hashmap(li, k):
    for i in range(1,len(li)):
        li[i] += li[i-1]
    map = {0:-1}
    max_len = 0
    for i in range(0, len(li)):
        if (li[i] - k) in map:
            max_len = max(max_len, i-map[li[i]-k])
        if li[i] not in map:
            map[li[i]] = i
    return max_len

class Solution(object):
    def maxSubArrayLen(self, nums, k, hashmap=True):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if hashmap:
            return max_sum_hashmap(nums, k)
        return max_sum_table(nums, k)

def test():
    import random
    dim = 10000
    test_li = [random.randint(1,dim) for _ in range(dim)]
    test = Solution()
    test.maxSubArrayLen(test_li, random.randint(1, dim), hashmap=True)

if __name__ == "__main__":
    import profile
    profile.run('test()')