class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = dict()
        for item in strs:
            sorted_word = "".join(sorted(item))
            if sorted_word not in result:
                result[sorted_word] = [item]
            else:
                result[sorted_word].append(item)
        return list(result.values())
            