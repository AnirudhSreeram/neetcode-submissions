class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = dict()
        dt = dict()
        for i in s:
            if i in ds:
                ds[i] += 1
            else:
                ds[i] = 1

        for j in t:
            if j in dt:
                dt[j] += 1
            else:
                dt[j] = 1
        
        if ds == dt:
            return True
        else:
            return False

        