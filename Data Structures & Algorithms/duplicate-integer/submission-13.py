class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for i in nums:
            if i in array:
                return true
            else:
                array.append(i)