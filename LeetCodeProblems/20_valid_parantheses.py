class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict1={")":"(", "}":"{", "]":"["}
        for i in s:
            if i in dict1.values():
                stack.append(i)
            elif i in dict1.keys():
                if stack==[] or dict1[i]!=stack.pop():
                    return False
            else:
                return True
s = Solution()
print(s.isValid("[(])")) 
            
