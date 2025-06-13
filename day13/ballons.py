class Solution(object):
    def maxNumberOfBalloons(self, text):
        b = a = l = o = n = 0
        for char in text:
            if char == 'b':
                b += 1
            elif char == 'a':
                a += 1
            elif char == 'l':
                l += 1
            elif char == 'o':
                o += 1
            elif char == 'n':
                n += 1
        l = l // 2
        o = o // 2
        return min(b, a, l, o, n)
    
hello=Solution()
answer=hello.maxNumberOfBalloons("loonbalxballpoon")
print(answer)
