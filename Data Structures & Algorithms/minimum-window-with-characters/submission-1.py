class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_cnt = {}
        window = {}
        for i in t:
            t_cnt[i] = 1 + t_cnt.get(i,0)
        
        need = len(t)
        have = 0
        result, res_len = [-1,-1], float("inf") 

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            
            if s[r] in t_cnt and window[s[r]] <= t_cnt[s[r]]:
                have += 1
            print(have, need)
            while have == need:
                if (r - l + 1) < res_len:
                    result = [l,r]
                    res_len = (r - l + 1)
            
                window[s[l]] -= 1
                if s[l] in t_cnt and window[s[l]] < t_cnt[s[l]]:
                    have -= 1
                l += 1
        return s[result[0]:result[1] + 1] if res_len != float('inf') else ""


         