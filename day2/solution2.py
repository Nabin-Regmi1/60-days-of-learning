class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new_nums=[0]*len(nums)
        for i in range(len(nums)):
            new_nums[(i+k)%len(nums)]=nums[i]
        for j in range(len(nums)):
            nums[j]=new_nums[j]
        return nums

hello = Solution()
number=[1,2,3,4,5,6,7]
answer=hello.rotate(number,3)
print(answer)