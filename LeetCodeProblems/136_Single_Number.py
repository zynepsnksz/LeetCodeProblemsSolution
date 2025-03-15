class Solution(object):
    def one_singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        #### O(n) and O(n)###
        array = []
        for i in nums:
            if i not in array:
                array.append(i)
            elif i in array:
                array.remove(i)
            return array[0]
        ### o(n) and 0(1) ###
    def two_singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        result = 0
        for i in nums:
            result ^= i
            return result
        
obj = Solution()
print(obj.one_singleNumber([4,1,2,1,2])) 
print(obj.two_singleNumber([4,1,2,1,2]))