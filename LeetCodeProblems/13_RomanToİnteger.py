class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        
        # Son karakteri ekle
        ans += roman[s[-1]]
        
        return ans

sayi = Solution()
print(sayi.romanToInt("LVIII"))  # 1994

# i in range(len(s)-1):
#             if roman[s[i]] < roman[s[i+1]]:
#                 ans = roman[s[i+1]] - roman[s[i]]
#             else:
#                 ans += roman[s[i]]  
#         return an