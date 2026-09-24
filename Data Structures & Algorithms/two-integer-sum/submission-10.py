class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for idx, num in enumerate(nums):
            compl = target - num
            if compl in complements:
                return [complements[compl], idx]
            
            complements[num] = idx

        return [] 