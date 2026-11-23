import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        prefix_product = 1
        postfix_product = 1

        result = []

        # creating the prefix array
        for num in nums:
            prefix_product *= num
            prefix.append(prefix_product)
        
        # creating the postfix array
        for num in reversed(nums):
            postfix_product *= num
            postfix.append(postfix_product)
        
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = postfix[len(nums)-i-2] if i < len(nums)-1 else 1

            value = left * right

            result.append(value)
        
        return result

        

