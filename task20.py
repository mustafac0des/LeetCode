class Solution:
    def isValid(self, s: str) -> bool:

        list_parenthesis = [""]
        
        i = 0
        while (True):
            if (len(s) == i): return False

            last_added = s[i]
            list_parenthesis.append(last_added)
            brackets = ["()", "[]", "{}"]

            if (list_parenthesis[-2]+s[i] in brackets): list_parenthesis = list_parenthesis[:-2]
            if (list_parenthesis == [""]): return True

            i += 1

