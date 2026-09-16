from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        answer = []
        sorted_freq = sorted(nums, key=lambda x: (-count[x], x))
        current_val = sorted_freq[0]
        answer.append(current_val)
        for val in sorted_freq:
            if k > 1 and val != current_val:
                answer.append(val)
                k -= 1
                current_val = val
            
        return answer
            
        

