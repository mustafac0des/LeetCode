class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        string=list(s)
        final_substrings=[]
        substring=""
        
        for i in range(len(string)):
            if substring.find(string[i])!=-1:
                final_substrings.append(substring)
                substring=string[i]
            else:
                substring=substring+string[i]

        result=1

        for i in final_substrings:
            if len(i)>result: result=len(i)
        
        return result