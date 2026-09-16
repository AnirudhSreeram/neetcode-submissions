class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ""
        for char in s:
            if char.isalnum():
                cleaned_text += char
        i = 0
        j = len(cleaned_text)-1
        cleaned_text = cleaned_text.lower()
        while i<=j:
            if cleaned_text[i] == cleaned_text[j]:
                i +=1
                j -=1
            else:
                return False
        return True