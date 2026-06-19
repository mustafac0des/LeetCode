class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        words = strs
        common = ""

        if ("" in words): return ""
        if (len(set(words)) <= 1): return words[0]

        min_index = 0

        for word in words:
            if (len(word) < min_index): min_index = len(word)

        i = 1
        isCommon = True
        prefixes = []

        while (isCommon == True):
            for word in words:
                prefixes.append(word[0:i])

            if (len(set(prefixes)) > 1): isCommon = False
            if (isCommon == True): common = prefixes[0]

            i += 1
            prefixes = []

        return common