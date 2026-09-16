class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0

        f_cnt = {}

        for r in range(len(s)):
            # get the most frequent count
            f_cnt[s[r]] = 1 + f_cnt.get(s[r],0)
            if r-l+1 - max(f_cnt.values()) <=k:
                result = max(result,r-l+1)
            else:
                f_cnt[s[l]] -= 1
                l += 1
        return result
