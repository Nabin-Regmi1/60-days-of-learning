class Solution:
    def reorganizeString(self, s):
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""
        freq_items = [[count, ch] for ch, count in freq.items()]
        result = []
        prev_char = ''
        prev_count = 0
        while freq_items:
            freq_items.sort(reverse=True)
            for i in range(len(freq_items)):
                count, ch = freq_items[i]
                if ch != prev_char:
                    result.append(ch)
                    prev_char = ch
                    freq_items[i][0] -= 1
                    if freq_items[i][0] == 0:
                        freq_items.pop(i)
                    break
            else:
                return "" 

        return ''.join(result)

hello=Solution()
answer=hello.reorganizeString("aab")
print(answer)