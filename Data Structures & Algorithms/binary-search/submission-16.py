class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        middle = (end + start) // 2

        while start <= end:
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
            middle = (end + start) // 2
            
        return -1

