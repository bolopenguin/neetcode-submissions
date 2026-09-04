class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        set_s = {}
        set_t = {}
        for char_s, char_t in zip(s,t):
            set_s[char_s] = set_s.get(char_s,0)+1
            set_t[char_t] = set_t.get(char_t,0)+1

        return set_s == set_t