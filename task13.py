class Solution:
    def romanToInt(self, s: str) -> int:
        s_roman = s
        s_int = 0

        while (s_roman != ""):
            if (s_roman[0] == "M"):
                s_int += 1000
                s_roman = s_roman[1:]
                continue

            if (s_roman[0:2] == "CM"):
                s_int += 900
                s_roman = s_roman[2:]
                continue

            if (s_roman[0:2] == "CD"):
                s_int += 400
                s_roman = s_roman[2:]
                continue

            if (s_roman[0] == "C"):
                s_int += 100
                s_roman = s_roman[1:]
                continue
            
            if (s_roman[0] == "D"):
                s_int += 500 
                s_roman = s_roman[1:]
                continue

            if (s_roman[0:2] == "XC"):
                s_int += 90
                s_roman = s_roman[2:]
                continue

            if (s_roman[0:2] == "XL"):
                s_int += 40
                s_roman = s_roman[2:]
                continue

            if (s_roman[0] == "X"):
                s_int += 10
                s_roman = s_roman[1:]
                continue
            
            if (s_roman[0] == "L"):
                s_int += 50 
                s_roman = s_roman[1:]
                continue

            if (s_roman[0:2] == "IX"):
                s_int += 9
                s_roman = s_roman[2:]
                continue

            if (s_roman[0:2] == "IV"):
                s_int += 4
                s_roman = s_roman[2:]
                continue

            if (s_roman[0] == "I"):
                s_int += 1
                s_roman = s_roman[1:]
                continue
            
            if (s_roman[0] == "V"):
                s_int += 5
                s_roman = s_roman[1:]
                continue
            
        return s_int