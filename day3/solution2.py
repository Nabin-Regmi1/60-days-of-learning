class Solution:
    def majorityElement(self,nums):
        count={}
        for i, num in enumerate(nums):
            if num in count:
                count[num]=1+count[num]
            else:
                count[num]=1
        for k in count:
            if count[k]>len(nums)//2:
                return k
        return []
    
hello=Solution()
answer=hello.majorityElement([1,2,3,4,5,2,2,2,2])
print(answer)