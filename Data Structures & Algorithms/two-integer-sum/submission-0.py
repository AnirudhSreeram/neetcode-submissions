class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = i 
        print(d) #{6: 0, 5: 1}
        for j in range(len(nums)):
            if nums[j] in d:
                t = d[nums[j]]
                if j!=t:
                    return [t,j]

            