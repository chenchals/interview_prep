class Solution(object):

    # O(N) solution O(N) complexity and O(N) memory
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        queue = []
        for i in range(size):
            j = size-1-i
            if nums[j] == 0:
                queue.append(nums[j])
            else:
                queue.insert(0, nums[j])
        nums[:] = queue[:]
    def old1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size):
            if nums[size-1-i] == 0:
                j = size-1-i
                # bubble sort
                # jth is 0, leave [j] untouch
                nums[:] = nums[:j]+nums[j+1:]+[0]
                # while j < size-1:
                #     j += 1
                #     buf = nums[j]
                #     nums[j] = nums[j-1]
                #     nums[j-1] = buf
        # print(nums)
        # return nums

test = Solution()
x = [0,1,0,3,12]
test.moveZeroes(x)
print(x)
answer = test.moveZeroes([2,1,0,1,0,4])
# print(answer)
answer = test.moveZeroes([-1,0,-3])
# print(answer)
