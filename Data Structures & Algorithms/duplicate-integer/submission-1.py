class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for i in nums:
            if i not in hash:
                hash.append(i)
            else:
                return true
