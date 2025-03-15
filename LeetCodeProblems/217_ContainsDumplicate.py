class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()  # Listeyi sıralıyoruz
        for i in range(len(nums) - 1):  # Son elemana kadar kontrol et
            if nums[i] == nums[i + 1]:  # Eğer ardışık iki eleman eşitse tekrar var
                return True
        return False  # Döngü tamamlandıysa tekrar yoktur

# Doğru çağırma şekli
a = Solution()
print(a.containsDuplicate([1, 2, 3, 1]))  # True
print(a.containsDuplicate([1, 2, 3, 4]))