class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = {}

        for num in nums:
            occurence[num] = occurence.get(num, 0) + 1

        top_k = sorted(
            occurence,
            key=occurence.get,
            reverse=True
        )[:k]

        return top_k