class Solution:
    def twoSum(self, nums, target):
        sol = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in sol:
                return [sol[diff], i]
            sol[num] = i
        return []
    
hello=Solution()
answer=hello.twoSum([1,2,3,4,5],9)
print(answer)