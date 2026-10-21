class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s[::-1] == t:
            return True
        else:
            return False
            
