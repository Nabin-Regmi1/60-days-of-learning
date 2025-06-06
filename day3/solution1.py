class Solution:
    def moveZeroes(self, nums):
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_count] = nums[i]
                if zero_count != i:
                    nums[i] = 0
                zero_count += 1
        
        return nums
    
hello=Solution()
answer=hello.moveZeroes([1,0,2,0,3,4,5])
print(answer)