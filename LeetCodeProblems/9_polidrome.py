
class Solution(object):
    def isPalindrome(self,x:int):   
        rightlef = str(x)
        tlefright = rightlef[::-1]
        if rightlef == tlefright:
            return True
        else:
            return False
    def palidrome(self,x:int):
        if x < 0 and x //10==0:
            return False
        else:
            y=0
            while y < x:
                y = y * 10 + x % 10
                x //= 10
            return x in (y, y // 10)
        
solution = Solution() 
print(solution.isPalindrome(12321)) # True
print(solution.palidrome(123456)) # False




