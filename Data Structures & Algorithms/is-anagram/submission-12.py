class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = {}
        seen_t = {}

        for char_s, char_t in zip(s,t):
            seen_s[char_s] = seen_s.get(char_s, 0) + 1
            seen_t[char_t] = seen_t.get(char_t, 0) + 1

        return seen_s == seen_t