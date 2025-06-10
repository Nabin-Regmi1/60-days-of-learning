class Solution(object): 
    def zeroFilledSubarray(self,nums):
        count = 0
        result = 0

        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0

        return result
hello=Solution()
answer=hello.zeroFilledSubarray([0,0,0,2,0,0])
print(answer)
