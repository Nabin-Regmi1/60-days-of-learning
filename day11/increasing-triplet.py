class Solution(object): 
    def increasingTriplet(self,nums):
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
            
        return False
    
hello=Solution()
answer=hello.increasingTriplet([2,1,5,0,4,6])
print(answer)
