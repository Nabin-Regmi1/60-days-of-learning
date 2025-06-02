class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0  
        for k in range(1, len(nums)):
            if (nums[k] != nums[j]):
                j += 1
                nums[j] = nums[k]
        del nums[j+1:]
        return nums,(j + 1)  
    
hello=Solution()
answer=hello.removeDuplicates([1,1,1,2,2,2,2,3,3,4,5,6,7])
print(f"{answer} {type(answer)}")

