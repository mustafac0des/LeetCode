class Solution:
    def isPalindrome(self, x: int) -> bool:

        if (x < 0): return False

        x_list = list(str(x))
        x_list.reverse()
        x_string = ""

        for i in range (len(x_list)):
            x_string += x_list[i]

        x_num = int(x_string)

        return True if x == x_num else False