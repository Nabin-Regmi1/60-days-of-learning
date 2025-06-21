class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                current = num
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest
    
hello=Solution()
answer=hello.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(answer)
