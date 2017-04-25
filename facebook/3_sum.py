def three_sum(nums, target):
    nums = sorted(nums)
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                ans.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while r > l and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif s > target:
                r -= 1
            else:
                l += 1
    return ans



ret = three_sum([1,0,-1,2], 0)
print(ret)