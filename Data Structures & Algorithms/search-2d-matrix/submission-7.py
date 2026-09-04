class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = set()
        for x in matrix:
            b = set(x)
            a = a.union(b)
        return target in a
        