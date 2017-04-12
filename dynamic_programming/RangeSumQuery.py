class NumArray(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		if len(nums) > 0:

			# self.table = [[0] * len(nums) for x in range(len(nums))]
			self.table = [0] * (len(nums)+1)
			self.table[1] = nums[0]
			for j in range(1, len(self.nums)):
				self.table[j+1] = self.table[j] + self.nums[j]
			print(self.table)


	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		if i <= j:
			return self.table[j+1] - self.table[i]
		else:
			return 0

