class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        combination = ""
        combinations = []

        keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        given_keys = []

        for i in range (len(digits)):
            given_keys.append(keys[int(digits[i])])

        length = len(digits)

        if (length == 1): 
            combinations = list(keys[int(digits[i])])

        if (length == 2):
            for i in range (len(given_keys[0])):
                for j in range (len(given_keys[1])):
                    combination = given_keys[0][i]+given_keys[1][j]
                    combinations.append(combination)

        if (length == 3):
            for i in range (len(given_keys[0])):
                for j in range (len(given_keys[1])):
                    for k in range (len(given_keys[2])):
                        combination = given_keys[0][i]+given_keys[1][j]+given_keys[2][k]
                        combinations.append(combination)
        
        if (length == 4):
            for i in range (len(given_keys[0])):
                for j in range (len(given_keys[1])):
                    for k in range (len(given_keys[2])):
                        for l in range (len(given_keys[3])):
                            combination = given_keys[0][i]+given_keys[1][j]+given_keys[2][k]+given_keys[3][l]
                            combinations.append(combination)

        return combinations
        