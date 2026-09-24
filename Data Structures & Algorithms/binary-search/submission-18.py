class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find(start, end):
            if start > end:
                return -1
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                return find(middle + 1, end)
            else:
                return find(start, middle - 1)


        return find(0, len(nums) -1 )