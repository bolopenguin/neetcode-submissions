from collections import deque 
class MinStack:

    def __init__(self):
        self._stack = deque()
        self._min_stack = deque()

    def push(self, val: int) -> None:
        self._stack.append(val)

        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
