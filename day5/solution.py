class Solution:
    def isPalindrome(self, s):
        filtered = []
        for char in s:
            if char.isalnum():
                filtered+=(char.lower())

        print(filtered)
        print(type(filtered))
        return filtered == filtered[::-1]

hello = Solution()
answer = hello.isPalindrome("A man, a plan, a canal: Panama")
print(answer)
