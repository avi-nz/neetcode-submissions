class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s[::-1] == s:
            return True
        return False
            
