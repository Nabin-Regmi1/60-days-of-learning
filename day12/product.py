class Solution(object):
    def productExceptSelf(self,nums):
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
    
        return answer
hello=Solution()
answer=hello.productExceptSelf([1,2,3,4])
print(answer)