import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_array = [0] * len(nums)
        result = []
        zero_count = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
            
            if zero_count > 1:
                result = [0] * len(nums)
                return result

        
        for i, number in enumerate(nums):
            if zero_count:
                if number:
                    value = 0
                else:
                    value = product
            else:
                value = product // number

            result.append(value)
        
        return result


