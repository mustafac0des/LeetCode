class Solution:
    def reverse(self, x: int) -> int:

        isPositive = True
        if (x < 0): 
            isPositive = False
            x = abs(x)

        x_list = list(str(x))
        x_list.reverse()

        result = ""

        
        if (x_list[0] != "0"): result = x_list[0]
        if (len(x_list) == 1): result = x_list[0]
        
        for i in range (1, len(x_list)):
            if (not len(x_list) > 1):
                break
            result = result + str(x_list[i])

        final_result = int(result) if isPositive else -1*int(result)

        return final_result if not (abs(final_result) > ((2**31)-1)) else 0