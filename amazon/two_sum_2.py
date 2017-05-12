# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.two_pointers(numbers, target)

    def two_pointers(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] == target:
                return left+1, right+1
            elif numbers[left]+numbers[right] > target:
                right -= 1
            else:
                left += 1
        return 0,0

    def binary_search_approach(self, numbers, target):
        for i in range(len(numbers)):
            print(i, len(numbers)-1)
            ret = self.binary_search(numbers, target-numbers[i], i+1, len(numbers)-1)
            # print(ret)
            if ret is not None and i != ret:
                return (i+1, ret+1)
        return 0,0



    def binary_search(self, numbers, target, start, end):
        if start > end:
            return None
        mid = int((start+end)/2)
        # print(start, mid, end)
        if numbers[mid] == target:
            return mid
        else:
            if numbers[mid] < target:
                return self.binary_search(numbers, target, mid+1, end)
            else:
                return self.binary_search(numbers, target, start, mid-1)



# test = Solution()
# ret = test.twoSum([1,2,3,4,4,9,56,90], 8)
# print(ret)