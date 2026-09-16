class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
        
            m = (l+r) // 2
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            elif nums[m] < nums[l]:
                res = min(res, nums[l])
                r = m
                
        return res