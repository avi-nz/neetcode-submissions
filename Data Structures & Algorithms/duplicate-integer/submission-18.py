class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_map = set()
        for i in nums:
            if i in number_map:
                return True
            else:
                number_map.add(i)
        
        return False