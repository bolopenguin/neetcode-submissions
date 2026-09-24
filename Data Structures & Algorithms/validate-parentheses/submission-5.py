class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchings = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for char in s:
            if char in matchings:
                stack.append(char)
            elif len(stack) == 0 or matchings[stack[-1]] !=char :
                return False
            else:
                stack.pop(-1)

        return len(stack) == 0