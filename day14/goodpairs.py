class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        freq = {}
        
        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count

hello=Solution()
answer=hello.numIdenticalPairs([1,2,3,1,1,3])
print(answer)