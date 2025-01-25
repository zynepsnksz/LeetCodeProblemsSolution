class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimal_a  = 0
        decimal_b = 0
        for num, char in enumerate(reversed(a)):  
            decimal_a += (2**num) * int(char)
        
        for num, char in enumerate(reversed(b)):
            decimal_b += (2**num) * int(char)
        total = decimal_a + decimal_b
        if total == 0:
            return "0"
        stack = []
        while total > 0:
            stack.append(str(total % 2))
            total //= 2
        return ''.join(reversed(stack))
s = Solution()
print(s.addBinary("11","1"))

