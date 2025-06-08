class Solution(object):
  def convert(self,s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        # Reverse direction if we're at the top or bottom
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Move up or down
        current_row += 1 if going_down else -1

    return ''.join(rows)
  
hello=Solution()
word="PAYPALISHIRING"
answer=hello.convert(word,3)
print(answer)
