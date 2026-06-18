class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = list(s)
        substring = ""
        final_substrings = []

        for i in range(len(string)):
            if substring.find(string[i]) != -1:
                final_substrings.append(substring)

                cut_index = substring.find(string[i])
                substring = substring[cut_index + 1:] + string[i]
                
            else:
                substring = substring + string[i]
        
        final_substrings.append(substring)

        result = 0
        
        for i in final_substrings:
            if len(i) >= result: 
                result = len(i)
        
        return result