class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==0:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones_sorted = sorted(stones, reverse=True)
        stone_one = stones_sorted[0]
        stone_two = stones_sorted[1]

        if stone_one == stone_two:
            stones_sorted.pop(0)
            stones_sorted.pop(0)
        elif stone_one < stone_two:
            stones_sorted[1] = stone_two - stone_one
            stones_sorted.pop(0)
        else:
            stones_sorted[0] = stone_one - stone_two
            stones_sorted.pop(1)
        
        return self.lastStoneWeight(stones_sorted)


