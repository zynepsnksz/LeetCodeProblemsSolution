def solution(nums):
    numbers={}
    caunter= 0
    max_num= 0
    for num in nums:
        numbers[num]= 1 + numbers.get(num,0)
        if numbers[num]>max_num:
            caunter = num
        max_num =max(max_num,numbers[num]) 
    return caunter  
print(solution([1,2,1,2,2,2,2,2]))
def boyer_Moore(nums):
    number=0
    caunter=0
    for num in range(len(nums)):
        if caunter==0 and number != nums[num]:
            number = nums[num]
            caunter +=1
        elif caunter!=0 and number != nums[num]:
            caunter -=1
        else:
            caunter +=1
    return number
print(boyer_Moore([2,2,3,1,1,1,3]))
def boyerMoore (nums):
    number=0
    caunter=0
    for num in nums:
        number = num if caunter == 0 else number
        caunter +=1 if num==number else -1
    return number

print(boyerMoore([1,1,2,2,2,1,1]))

            

