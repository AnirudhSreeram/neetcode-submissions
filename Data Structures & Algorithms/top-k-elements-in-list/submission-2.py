class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fre = [[] for n in range(len(nums)+1) ]

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        for key , v in count.items():
            fre[v].append(key)

        result = []
        for i in range(len(fre) - 1, 0, -1):
            for f in fre[i]:
                result.append(f)
                if len(result) == k:
                    return result