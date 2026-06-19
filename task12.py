class Solution:
    def thousandsToRoman(self, num: str) -> str:
        return int(num)*"M"

    def hundredsToRoman(self, num: str) -> str:
        if (num == "9"): return "CM"
        if (num == "4"): return "CD"
        if (int(num) < 4): return int(num)*"C"
        if (int(num) == 5): return "D"
        if (int(num) > 5): return "D"+("C"*(int(num)-5))

    def tensToRoman(self, num: str) -> str:
        if (num == "9"): return "XC"
        if (num == "4"): return "XL"
        if (int(num) < 4): return int(num)*"X"
        if (int(num) == 5): return "L"
        if (int(num) > 5): return "L"+("X"*(int(num)-5))

    def unitsToRoman(self, num: str) -> str:
        if (num == "9"): return "IX"
        if (num == "4"): return "IV"
        if (int(num) < 4): return int(num)*"I"
        if (int(num) == 5): return "V"
        if (int(num) > 5): return "V"+("I"*(int(num)-5))

    def intToRoman(self, num: int) -> str:
        num_string = str(num)
        num_roman = ""

        index_num = len(num_string)

        if (index_num == 4): 
            num_roman += self.thousandsToRoman(num_string[0])
            num_string = num_string[1:]
            index_num = index_num - 1

        if (index_num == 3): 
            num_roman += self.hundredsToRoman(num_string[0])
            num_string = num_string[1:]
            index_num = index_num - 1

        if (index_num == 2): 
            num_roman += self.tensToRoman(num_string[0])
            num_string = num_string[1:]
            index_num = index_num - 1

        if (index_num == 1): 
            num_roman += self.unitsToRoman(num_string[0])

        return num_roman