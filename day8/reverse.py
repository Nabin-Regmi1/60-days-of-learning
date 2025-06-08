class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split(' ')
        print(words)
        reversed_words = words[::-1]
        #print(type(reversed_words))
        #print(reversed_words)
        return ' '.join(reversed_words)
hello=Solution()
answer=hello.reverseWords("the sky is blue")
print(answer)