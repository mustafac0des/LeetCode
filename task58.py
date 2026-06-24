class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        words = s.split()
        last_word = words[len(words) - 1]

        return len(last_word)
        