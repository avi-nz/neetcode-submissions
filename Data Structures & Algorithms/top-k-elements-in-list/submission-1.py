class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        top_k = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:k]

        return [key for key, value in top_k]