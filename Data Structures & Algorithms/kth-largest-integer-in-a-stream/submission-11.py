class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
    
    def _insert(self, val):
        if len(self.nums )== 0:
            self.nums.append(val)
            return
        if val <= self.nums[0]:
            self.nums.insert(0,val)
            return
        if val >= self.nums[-1]:
            self.nums.append(val)
            return

        for idx in range(len(self.nums) -1):
            if val >= self.nums[idx] and val < self.nums[idx +1]:
                self.nums.insert(idx + 1, val)
                return

    def add(self, val: int) -> int:
        self._insert(val)

        return self.nums[-self.k]
        