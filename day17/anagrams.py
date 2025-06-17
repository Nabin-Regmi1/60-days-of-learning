class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())

hello=Solution()
word=["eat","tea","tan","ate","nat","bat"]
answer=hello.groupAnagrams(word)
print(answer)