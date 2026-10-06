class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in anagrams:
                anagrams[word_sorted] = []
            anagrams[word_sorted].append(word)
        
        return list(anagrams.values())