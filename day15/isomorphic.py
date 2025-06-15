class Solution(object):
    def isIsomorphic(self,s, t):
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            else:
                map_s_t[char_s] = char_t

            if char_t in map_t_s:
                if map_t_s[char_t] != char_s:
                    return False
            else:
                map_t_s[char_t] = char_s

        return True
hello=Solution()
answer=hello.isIsomorphic("paper","title")
print(answer)