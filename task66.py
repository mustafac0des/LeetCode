class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits_string = ""

        for i in range (len(digits)):
            digits_string += str(digits[i])
        
        digits_string_plus_one = str(int(digits_string) + 1)
        digits_list = list(digits_string_plus_one)

        for i in range (len(digits_list)):
            digits_list[i] = int(digits_list[i])

        return digits_list